__author__ = 'assafalon'
#first mate:
dom = 17
hetro = 25
rec = 15
total = float(dom + hetro + rec)

#rec * rec
P1 = (rec/total)*((rec-1)/(total-1))
# rec * hetro or the other way around
P2 = (rec/total)*(hetro/(total-1))
# hetro * hetro
P3 = (hetro/total)*((hetro-1)/(total-1))*0.25
P_total = 1 - P1 - P2 -P3
print P_total