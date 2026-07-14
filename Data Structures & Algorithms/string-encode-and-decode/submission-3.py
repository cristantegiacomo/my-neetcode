class Solution:

    def encode(self, strs: List[str]) -> str:
        stringa_tot=""
        for i,s in enumerate(strs):
            for j,c in enumerate(s):
                stringa_tot+=str(ord(c))+"."#+str(i)+","+str(j)+"." 
            stringa_tot+="|"
        return stringa_tot


    def decode(self, s: str) -> List[str]:
        lista_str=s.split("|")
        lista_str.pop()
        res=[]
        for stringa in lista_str:
            cars=stringa.split(".")
            cars.pop()
            parola=""
            for car in cars:
                parola+=chr(int(car))
            res.append(parola)
        return res






