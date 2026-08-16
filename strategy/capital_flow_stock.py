"""
资金流向选股策略
================
筛选当天资金净流入最多、且有大单（>=100万）流入的股票。
用于游资隔夜持仓策略的选股环节。

数据源：AKShare（免费，无需注册）
输出：控制台表格 + CSV文件

用法：
    python strategy/capital_flow_stock.py
    python strategy/capital_flow_stock.py --top 30   # 显示前30只
"""

import akshare as ak
import pandas as pd
from datetime import datetime
from loguru import logger
import os
import argparse


# ============== 配置参数 ==============
DEFAULT_TOP_N = 20          # 默认显示前N只股票
OUTPUT_DIR = "output"       # CSV输出目录
MIN_MAIN_FLOW = 0           # 主力净流入最低阈值（元），0表示必须净流入
MIN_SUPER_LARGE_FLOW = 0    # 超大单净流入最低阈值（元）
# ======================================


def get_capital_flow_data():
    """
    获取全市场个股今日资金流向数据

    Returns:
        pd.DataFrame: 资金流向数据，按主力净流入降序排列
    """
    logger.info("正在获取全市场资金流向数据...")

    try:
        # 获取今日个股资金流向排名
        df = ak.stock_individual_fund_flow_rank(indicator="今日")
        logger.info(f"成功获取 {len(df)} 只股票的资金流向数据")
        return df
    except Exception as e:
        logger.error(f"获取资金流向数据失败: {e}")
        raise


def filter_and_sort(df, top_n=DEFAULT_TOP_N):
    """
    筛选并排序股票

    筛选条件：
    1. 主力净流入 > 0（资金净买入）
    2. 超大单净流入 > 0（有机构/游资大资金参与）

    Args:
        df: 原始资金流向数据
        top_n: 返回前N只股票

    Returns:
        pd.DataFrame: 筛选排序后的股票列表
    """
    logger.info("开始筛选股票...")

    # 打印列名用于调试
    logger.debug(f"数据列名: {df.columns.tolist()}")

    # 标准化列名（处理可能的列名变化）
    column_mapping = {}
    for col in df.columns:
        col_lower = col.lower()
        if '代码' in col or 'code' in col_lower:
            column_mapping[col] = '代码'
        elif '名称' in col or 'name' in col_lower:
            column_mapping[col] = '名称'
        elif '最新价' in col or '收盘' in col:
            column_mapping[col] = '最新价'
        elif '涨跌幅' in col:
            column_mapping[col] = '涨跌幅'
        elif '主力' in col and '净额' in col and '净占比' not in col:
            column_mapping[col] = '主力净流入'
        elif '超大单' in col and '净额' in col and '净占比' not in col:
            column_mapping[col] = '超大单净流入'
        elif '大单' in col and '净额' in col and '净占比' not in col and '超大单' not in col:
            column_mapping[col] = '大单净流入'

    df = df.rename(columns=column_mapping)

    # 检查必要的列是否存在
    required_cols = ['代码', '名称', '主力净流入']
    missing_cols = [col for col in required_cols if col not in df.columns]
    if missing_cols:
        logger.error(f"数据缺少必要的列: {missing_cols}")
        logger.error(f"当前列名: {df.columns.tolist()}")
        return pd.DataFrame()

    # 确保数值列为数字类型
    numeric_cols = ['最新价', '涨跌幅', '主力净流入', '超大单净流入', '大单净流入']
    for col in numeric_cols:
        if col in df.columns:
            df[col] = pd.to_numeric(df[col], errors='coerce')

    # 筛选条件1：主力净流入 > 0
    df_filtered = df[df['主力净流入'] > MIN_MAIN_FLOW].copy()
    logger.info(f"主力净流入 > 0 的股票: {len(df_filtered)} 只")

    # 筛选条件2：超大单净流入 > 0（如果列存在）
    if '超大单净流入' in df_filtered.columns:
        df_filtered = df_filtered[df_filtered['超大单净流入'] > MIN_SUPER_LARGE_FLOW]
        logger.info(f"超大单净流入 > 0 的股票: {len(df_filtered)} 只")

    # 按主力净流入降序排列
    df_filtered = df_filtered.sort_values('主力净流入', ascending=False)

    # 取前N只
    result = df_filtered.head(top_n)
    logger.info(f"筛选出 Top {len(result)} 只股票")

    return result


def format_amount(value):
    """
    格式化金额为易读格式（万/亿）

    Args:
        value: 金额（元）

    Returns:
        str: 格式化后的金额字符串
    """
    if pd.isna(value):
        return "-"
    abs_value = abs(value)
    if abs_value >= 1e8:
        return f"{value / 1e8:.2f}亿"
    elif abs_value >= 1e4:
        return f"{value / 1e4:.2f}万"
    else:
        return f"{value:.2f}"


def display_results(df):
    """
    在控制台以表格形式展示结果

    Args:
        df: 筛选后的股票数据
    """
    if df.empty:
        logger.warning("没有符合条件的股票")
        return

    print("\n" + "=" * 80)
    print(f"  📊 资金流向选股结果 - {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("=" * 80)

    # 选择要显示的列
    display_cols = ['代码', '名称']
    if '最新价' in df.columns:
        display_cols.append('最新价')
    if '涨跌幅' in df.columns:
        display_cols.append('涨跌幅')
    if '主力净流入' in df.columns:
        display_cols.append('主力净流入')
    if '超大单净流入' in df.columns:
        display_cols.append('超大单净流入')
    if '大单净流入' in df.columns:
        display_cols.append('大单净流入')

    display_df = df[display_cols].copy()

    # 格式化数值
    if '涨跌幅' in display_df.columns:
        display_df['涨跌幅'] = display_df['涨跌幅'].apply(
            lambda x: f"{x:.2f}%" if not pd.isna(x) else "-"
        )

    if '最新价' in display_df.columns:
        display_df['最新价'] = display_df['最新价'].apply(
            lambda x: f"{x:.2f}" if not pd.isna(x) else "-"
        )

    for col in ['主力净流入', '超大单净流入', '大单净流入']:
        if col in display_df.columns:
            display_df[col] = display_df[col].apply(format_amount)

    # 打印表格
    print(display_df.to_string(index=False))
    print("=" * 80)
    print(f"  共 {len(display_df)} 只股票")
    print("=" * 80 + "\n")


def save_to_csv(df):
    """
    保存结果到CSV文件

    Args:
        df: 筛选后的股票数据
    """
    if df.empty:
        logger.warning("没有数据可保存")
        return

    # 创建输出目录
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    # 生成文件名
    date_str = datetime.now().strftime('%Y%m%d_%H%M%S')
    filename = f"capital_flow_top_stocks_{date_str}.csv"
    filepath = os.path.join(OUTPUT_DIR, filename)

    # 保存CSV（使用utf-8-sig编码，Excel打开中文不乱码）
    df.to_csv(filepath, index=False, encoding='utf-8-sig')
    logger.info(f"结果已保存到: {filepath}")


def main():
    """主函数"""
    # 解析命令行参数
    parser = argparse.ArgumentParser(description='资金流向选股策略')
    parser.add_argument('--top', type=int, default=DEFAULT_TOP_N,
                        help=f'显示前N只股票（默认: {DEFAULT_TOP_N}）')
    args = parser.parse_args()

    logger.info("=" * 50)
    logger.info("  资金流向选股策略启动")
    logger.info("=" * 50)

    try:
        # 1. 获取数据
        df = get_capital_flow_data()

        # 2. 筛选排序
        result = filter_and_sort(df, top_n=args.top)

        if result.empty:
            logger.warning("未找到符合条件的股票，请检查市场数据或调整筛选条件")
            return

        # 3. 展示结果
        display_results(result)

        # 4. 保存到CSV
        save_to_csv(result)

        logger.info("选股完成！")

    except Exception as e:
        logger.error(f"选股过程出错: {e}")
        raise


if __name__ == '__main__':
    main()
