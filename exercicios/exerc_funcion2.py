def reloj(hour=None, min=None, seg=None):
	if hour == None and min==None:
        h = seg/3600
        seg = seg%3600
        m = seg//60
        seg = seg%60
        return h,m,seg

    else:
        if hour != None:
            segh = hour*3600
        else:
            segh = 0
        if min != None:
            segM =min*60
        else:   
            segM = 0
        if seg != None:
            segS =seg
        else:
            segS = 0
        segTot = segh+segM+segS

print("la hora es")
print(reloj(seg=3600))