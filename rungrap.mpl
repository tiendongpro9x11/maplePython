plotsetup(default):
interface(plotdevice):
plotsetup(tek,kermit):
plotsetup(ps,plotoutput=`plot.ps`,plotoptions=`portrait, noborder, width=1000, height=500`):
plotsetup(x11):
plotsetup(maplet):
plot([((3)*x^2+(2)*x+(1))/((2)*x+(3)),3/2*x-5/4],x,color=["Red","Red"]);