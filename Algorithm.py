from scikitmcda.topsis import TOPSIS
from scikitmcda.dmuu import DMUU
from scikitmcda.wsm import WSM
from scikitmcda.wpm import WPM
from scikitmcda.waspas import WASPAS
from scikitmcda.promethee_ii import PROMETHEE_II
from scikitmcda.constants import MAX, MIN, LinearMinMax_, LinearMax_, LinearSum_, Vector_, EnhancedAccuracy_, Logarithmic_ 

class Decision_Algorithm:
    def __init__(self):
        self.Matrix=[]
        self.alternatives=[]
        self.states=[]
        
    def add(self,Matrix,alternatives,states):
        self.Matrix=Matrix
        self.alternatives=alternatives
        self.states=states
        
    def Rankwithtopsis(self,Matrix,alternatives,states):
        topsis = TOPSIS()

        topsis.dataframe(Matrix,
                         alternatives,
                         states
                         )
        print(topsis.pretty_original())
        w_AHP = topsis.set_weights_by_AHP([[  1,    4,    5,   7],   # C1
                                       [1/4,    1,    3,   5],   # C2
                                       [1/5,  1/3,    1,   3],   # C3
                                       [1/7,  1/5,  1/3,   1]])  # C4
        print("AHP Returned:\n", w_AHP)
        topsis.set_signals([MIN, MAX, MAX, MAX])

        topsis.decide()

        print("WEIGHTS:\n", topsis.weights)
        print("NORMALIZED:\n", topsis.pretty_normalized())

        print("WEIGHTED:\n", topsis.pretty_weighted())

        topsis.decide(EnhancedAccuracy_)
        print("RANKING TOPSIS with", topsis.normalization_method, ":\n", topsis.pretty_decision())
        
    def print_table(self,x):
        x=x.replace("-","")
        x=x.replace("+","")
        x=x.replace("|","")
        x=x.replace("DMUU"," ")
        x=x.split("\n")
        m=[]
        List=[]
        for k in range(0,len(x)):
            if x[k]!="":
                m.append(x[k])
        for i in range(0,len(m)):
            List.append(m[i].split()) 
        column_names=[]
        data=[]
        for i in range(0,len(List)):
            if i==0:
                column_names=List[i][:5] 
            else:
                for j in range(0,len(List[i])):
                    if j>=4:
                        string="".join(List[i][4:])
                        data.append(string)
                        break
                    else:
                        data.append(List[i][j])

        dic={}

        for i in range(0,len(column_names)):
            dic[column_names[i]]=[data[i]]

        for x,y in dic.items():
            print(x," : ",y)
            
    # Specifying the criteria method
    def minimax_regret(self,Matrix,
                    alternatives,
                    states):
        dmuu = DMUU()
        dmuu.dataframe(Matrix,
                        alternatives,
                        states
                        )
        dmuu.minimax_regret()

        print(dmuu.pretty_calc())

        x=dmuu.pretty_decision()
        self.print_table(x)

# Specifying the criteria method
    def maximax(self,Matrix,
                    alternatives,
                    states):
        dmuu=DMUU()
        dmuu.dataframe(Matrix,
                        alternatives,
                        states
                        )
        dmuu.maximax()
        print(dmuu.pretty_calc())
        x=dmuu.pretty_decision()
        self.print_table(x)

    # Specifying the criteria method
    def maximin(self,Matrix,
                    alternatives,
                    states):
        dmuu=DMUU()
        dmuu.dataframe(Matrix,
                        alternatives,
                        states
                        )
        dmuu.maximin()
        print(dmuu.pretty_calc())
        x=dmuu.pretty_decision()
        self.print_table(x)

    # Specifying the criteria method
    def hurwicz(self,Matrix,
                    alternatives,
                    states):
        dmuu=DMUU()
        dmuu.dataframe(Matrix,
                        alternatives,
                        states
                        )
        dmuu.hurwicz()
        print(dmuu.pretty_calc())
        x=dmuu.pretty_decision()
        self.print_table(x)

    # Specifying the criteria method
    def laplace(self,Matrix,
                    alternatives,
                    states
                    ):
        dmuu=DMUU()
        dmuu.dataframe(Matrix,
                        alternatives,
                        states
                        )
        dmuu.laplace()
        print(dmuu.pretty_calc())
        x=dmuu.pretty_decision()
        self.print_table(x)
    