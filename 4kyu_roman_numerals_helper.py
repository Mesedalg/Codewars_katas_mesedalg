# https://www.codewars.com/kata/51b66044bce5799a7f000003
class RomanNumerals:
    def to_roman(val):
        l=[0,1,2,3,4,5,6,7,8,9]
        r=["","I","II","III","IV","V","VI","VII","VIII","IX"]
        nums=r[l.index(val%10)]
        return ("M"*(val//1000)+"CM"*(val%1000//900)+"D"*(val%1000%900//500)
        +"CD"*(val%1000%900%500//400)+"C"*(val%1000%900%500%400//100)
        +"XC"*(val%100//90)+"L"*(val%100%90//50)+"XL"*(val%100%90%50//40)
        +"X"*(val%100%90%50%40//10)+nums)

    def from_roman(r):
        num=0
        l=[9, 8, 7, 6, 4, 3, 2, 1]
        r2=['IX', 'VIII', 'VII', 'VI', 'IV', 'III', 'II', 'I']
        if r.count("V")==1 and r.count("I")==0:
            num=5
        else:
            for i in r2:
                if r.count(i)==1:
                    num=l[r2.index(i)]
                    break
        return (1000*(r.count("M")-r.count("CM"))
            +900*r.count("CM")+500*(r.count("D")-r.count("CD"))+400*r.count("CD")
            +100*(r.count("C")-r.count("XC")-r.count("CM")-r.count("CD"))
            +90*r.count("XC")+50*(r.count("L")-r.count("XL"))+40*r.count("XL")
            +10*(r.count("X")-r.count("XL")-r.count("XC")-r.count("IX"))
            +num)