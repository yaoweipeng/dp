import numpy
import matplotlib.pyplot as pyplot
pyplot.style.use('seaborn-paper')
# pyplot.rcParams['font.size'] = 24

def cm2inch(value):
    return value/2.54

# fig = plt.figure(figsize=(cm2inch(12.8), cm2inch(9.6)))


mer_pho_num = numpy.loadtxt('mer_pho_num.txt',dtype='int')
mer_electron_num = numpy.loadtxt('mer_electron_num.txt',dtype='int') + 2500
mer_positron_num = numpy.loadtxt('mer_positron_num.txt',dtype='int')

nomer_pho_num = numpy.loadtxt('nomer_pho_num.txt',dtype='int')
nomer_electron_num = numpy.loadtxt('nomer_electron_num.txt',dtype='int') + 2500
nomer_positron_num = numpy.loadtxt('nomer_positron_num.txt',dtype='int')


def make_patch_spines_invisible(ax):
    ax.set_frame_on(True)
    ax.patch.set_visible(False)
    for sp in ax.spines.values():
        sp.set_visible(False)


fig, host = pyplot.subplots(figsize=(cm2inch(8.5),cm2inch(6)))
fig.subplots_adjust(right=0.8)  # ???
# fig.set_figure(cm2inch(8.5), cm2inch(6))

par1 = host.twinx()
par2 = host.twinx()

# Offset the right spine of par2.  The ticks and label have already been
# placed on the right by twinx above.
par2.spines["right"].set_position(("axes", 1.3))
# Having been created by twinx, par2 has its frame off, so the line of its
# detached spine is invisible.  First, activate the frame but make the patch
# and spines invisible.
make_patch_spines_invisible(par2)
# Second, show the right spine.
par2.spines["right"].set_visible(True)


p1, = host.plot(nomer_electron_num[0:1000:40]/1e4, "b-", lw=1, label="w/o merging")
p2, = par1.plot(nomer_positron_num[0:1000:40]/1e4, "g-", lw=1, label="w/o merging")
p3, = par2.plot(nomer_pho_num[0:1000:40]/1e6, "r-", lw=1, label="w/o merging")

p11, = host.plot(mer_electron_num[0:1000:40]/1e4, "bo", lw=1, markersize=3, markeredgewidth=1, markeredgecolor='b', markerfacecolor='None',label="w merging")
p22, = par1.plot(mer_positron_num[0:1000:40]/1e4, "go", lw=1, markersize=3, markeredgewidth=1, markeredgecolor='g', markerfacecolor='None',label="w merging")
p33, = par2.plot(mer_pho_num[0:1000:40]/1e6, "ro", lw=1, markersize=3, markeredgewidth=1, markeredgecolor='r', markerfacecolor='None',label="w merging")

host.set_xlim(0,25)
host.set_ylim(0,2)
par1.set_ylim(0,2)
par2.set_ylim(0,2)

host.set_xlabel("time($\omega_{pe}^{-1}$)")
host.set_ylabel("Number of Electrons[x$10^4$]")
par1.set_ylabel("Number of Positrons[x$10^4$]")
par2.set_ylabel("Number of Photons[x$10^6$]")

host.yaxis.label.set_color(p1.get_color())
par1.yaxis.label.set_color(p2.get_color())
par2.yaxis.label.set_color(p3.get_color())

tkw = dict(size=4, width=1.5)
tkwx = dict(size=5, width=1.5)
host.tick_params(axis='x', **tkwx)
host.tick_params(axis='y', colors=p1.get_color(), **tkw)
par1.tick_params(axis='y', colors=p2.get_color(), **tkw)
par2.tick_params(axis='y', colors=p3.get_color(), **tkw)

lines = [p1,p2,p3,p11,p22,p33]

# host.legend(lines, [l.get_label() for l in lines],loc='best',numpoints=1, fancybox=True)

# pyplot.show()
pyplot.savefig('Merge_number1.pdf',bbox_inches='tight')  # n means normalized
# pyplot.close()



