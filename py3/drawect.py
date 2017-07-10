import matplotlib.pyplot as plt
import numpy as np


plt.style.use('seaborn-white')
# plt.rcParams['font.family'] = 'sans-serif'
# plt.rcParams['font.sans-serif'] = 'Tahoma'
# # plt.rcParams['font.monospace'] = 'Ubuntu Mono'
plt.rcParams['font.size'] = 16
# plt.rcParams['axes.labelsize'] = 10
# plt.rcParams['axes.labelweight'] = 'bold'
# plt.rcParams['xtick.labelsize'] = 8
# plt.rcParams['ytick.labelsize'] = 8
# plt.rcParams['legend.fontsize'] = 10
# plt.rcParams['figure.titlesize'] = 12

time = np.load('time.npy')

# TeC1 = np.load('tec1.npy')
TeS1 = np.load('tes1.npy')
# TeC2 = np.load('tec2.npy')
# TeS2 = np.load('tes2.npy')
# TeS3 = np.load('tes3.npy')
# TeC3 = np.load('tec3.npy')
# TeS3 = np.load('tes3.npy')
# TeC4 = np.load('tec4.npy')
# TeS4 = np.load('tes4.npy')
# TfeC1 = np.load('tfec1.npy')
# TfeS1 = np.load('tfes1.npy')
# TfeC2 = np.load('tfec2.npy')
# TfeS2 = np.load('tfes2.npy')
# TpeC1 = np.load('tpec1.npy')
# TpeS1 = np.load('tpes1.npy')
# TpeC2 = np.load('tpec2.npy')
# TpeS2 = np.load('tpes2.npy')

# dec1 = (TeC1-TeC1[0])/TeC1[0]
# des1 = (TeS1-TeS1[0])/TeS1[0]
# dec2 = (TeC2-TeC2[0])/TeC2[0]
# des2 = (TeS2-TeS2[0])/TeS2[0]
# des3 = (TeS3-TeS3[0])/TeS3[0]
# dec3 = (TeC3-TeC3[0])/TeC3[0]
# des3 = (TeS3-TeS3[0])/TeS3[0]
# dec4 = (TeC4-TeC4[0])/TeC4[0]
# des4 = (TeS4-TeS4[0])/TeS4[0]

plt.figure(figsize=(8,5))
ax = plt.subplot()
# ax.semilogy(time, dec1*100,'r-',   lw=2, label='$\gamma=1.1$-cal')
ax.plot(time, TeS1,'r-',  lw=2, label='$ppc=50$')
# ax.semilogy(time, dec2*100,'b-',   lw=2, label='$\gamma=5$-cal')
# ax.plot(time, TeS2,'b--',  lw=2, label='$ppc=50$')
# ax.plot(time, TeS3,'m:',  lw=2, label='$ppc=500$')
# # ax.semilogy(time, dec3*100,'g-',   lw=2, label='$\gamma=50$-cal')
# ax.semilogy(time, des3*100,'g--',  lw=2, label='$\gamma=50$-sys')
# # ax.semilogy(time, dec4*100,'m-',   lw=2, label='$\gamma=500$-cal')
# ax.semilogy(time, des4*100,'m--',  lw=2, label='$\gamma=500$-sys')
plt.xlabel('time($\omega_{pe}^{-1}$)',fontsize=24)
plt.ylabel('$E$ in $J$',fontsize=24)
plt.legend(loc='best', numpoints=1, fancybox=True, fontsize=10)
plt.grid(b=True,which='major',axis='both')
plt.title('energy conservation',fontsize=32,fontstyle='normal')

# plt.show()
plt.savefig('EneCons.png',bbox_inches='tight')  # n means normalized
plt.close()