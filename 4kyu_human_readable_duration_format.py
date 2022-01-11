# https://www.codewars.com/kata/52742f58faf5485cae000b9a
def prin(num,name,):
    if num!=0:
        if num > 1:
            return str(num)+name+"s&"
        else:
            return str(num)+name+"&"
    return "_"

def form(ls):
    if ls.count("_")==5:
        return "now"
    elif ls.count("_")==4:
        return ''.join(ls).replace("_","").replace("&","",1)
    elif ls.count("_")==3:
        return ''.join(ls).replace("_","").replace("&"," and ",1).replace("&","",1)
    elif ls.count("_")==2:
        return ''.join(ls).replace("_","").replace("&",", ",1).replace("&"," and ",1).replace("&","",1)
    elif ls.count("_")==1:
        return ''.join(ls).replace("_","").replace("&",", ",2).replace("&"," and ",1).replace("&","",1)
    else:
        return ''.join(ls).replace("_","").replace("&",", ",3).replace("&"," and ",1).replace("&","",1)
        


def format_duration(seconds):
    ls=[]
    ls.append(prin(seconds//31536000," year"))
    ls.append(prin(seconds//86400%365," day"))
    ls.append(prin(seconds%86400//3600," hour"))
    ls.append(prin(seconds%3600//60," minute"))
    ls.append(prin(seconds%60," second"))
    return form(ls)