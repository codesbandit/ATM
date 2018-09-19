inptJmlh = input("Jumlah uang anda = ")
hasil=inptJmlh/100000
sisa=inptJmlh%100000
print "Jumlah uang pecahan anda"
print hasil, "seratusribuan"
if (inptJmlh==100000):
    print hasil, "seratusribuan"
if (sisa>=50000):
    hasil=sisa/50000
    sisa=sisa%50000
    print hasil, "limapuluhribuan"
if (sisa>=20000):
    hasil=sisa/20000
    sisa=sisa%20000
    print hasil, "duapuluhribuan"
if (sisa>=10000):
    hasil=sisa/10000
    sisa=sisa%10000
    print hasil, "sepuluhribuan"

    # else:
    #     print "Error"
