import pandas as pd


def generate_auto_clean_report(cleaning_log):

    report_df = pd.DataFrame(cleaning_log)

    return report_df