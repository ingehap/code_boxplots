import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import lasio

def make_plots(df, log_name, png_name, dpi_val = 600, log_scale=False):
    vals = df[log_name].squeeze().to_numpy()
    f, (ax_box, ax_hist) = plt.subplots(2, sharex=True, gridspec_kw={"height_ratios": (.15, .85)})
    sns.boxplot(x=vals, ax=ax_box)
    sns_hp = sns.histplot(x=vals, bins=12, kde=True, stat='density', ax=ax_hist)
    ax_box.set(yticks=[])
    sns.despine(ax=ax_hist)
    sns.despine(ax=ax_box, left=True)
    sns_hp.set(xlabel=log_name)
    if log_scale:
        sns_hp.set_xscale("log")
    plt.savefig(png_name, dpi=dpi_val)

def LFP_CALI(df):
    make_plots(df, 'LFP_CALI', '../result/lfp_cali.png')

def LFP_DRHO(df):
    make_plots(df, 'LFP_DRHO', '../result/lfp_drho.png')

def LFP_DT_LOG(df):
    make_plots(df, 'LFP_DT_LOG', '../result/lfp_dt_log.png')

def LFP_DTS_LOG(df):
    make_plots(df, 'LFP_DTS_LOG', '../result/lfp_dts_log.png')

def LFP_DTST_LOG(df):
    make_plots(df, 'LFP_DTST_LOG', '../result/lfp_dtst_log.png')

def LFP_GR(df):
    make_plots(df, 'LFP_GR', '../result/lfp_gr.png')

def LFP_K(df):
    make_plots(df, 'LFP_K', '../result/lfp_k.png')

def LFP_NPHI(df):
    make_plots(df, 'LFP_NPHI', '../result/lfp_nphi.png')

def LFP_PEF(df):
    make_plots(df, 'LFP_PEF', '../result/lfp_pef.png')

def LFP_RHOB_LOG(df):
    make_plots(df, 'LFP_RHOB_LOG', '../result/lfp_rhob_log.png')

def LFP_RM(df):
    make_plots(df, 'LFP_RM', '../result/lfp_rm.png', log_scale=True)

def LFP_RS(df):
    make_plots(df, 'LFP_RS', '../result/lfp_rs.png', log_scale=True)

def LFP_RT_LOG(df):
    make_plots(df, 'LFP_RT_LOG', '../result/lfp_rt_log.png', log_scale=True)

def LFP_TH(df):
    make_plots(df, 'LFP_TH', '../result/lfp_th.png')

def LFP_U(df):
    make_plots(df, 'LFP_U', '../result/lfp_u.png')

