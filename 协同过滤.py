#UTF-8
#协同过滤
import math
import operator

class recommendation():
    def __init__(self,sample,name,choice=1,topk=1):
        self.sample=sample
        self.choice=choice
        self.topk=topk
        self.name=name
#运用集合去重
    def houxuanren(self):
        x=[]
        y=set()
        if self.name not in self.sample.keys():
            print('%s is not contains in our record' %(self.name))
        else:
            a = set(dic[self.name].keys())
            for i in self.sample.keys():
               b = set(self.sample[i].keys())
               #候选人必须看过待推荐人的所有电影
               if a==a&b and i!=self.name:
                   x.append(i)
                   y=y|(b-a)
        print('候选人包括：%s' %(x))
        print('候选电影包括：%s' %(y))
        y=list(y)
        return x,y

    def recommend(self):
        x,y=self.houxuanren()
        d=self.欧式距离()
        ini=0
        #计算所有人的加权推荐度（有点复杂的列表推倒）
        TOPlist=[(y1,
                  sum([float(self.sample[x1][y1])*float(d[x1]) for x1 in x if self.sample[x1].get(y1)!=None])
                 /sum([float(d[x1]) for x1 in x if self.sample[x1].get(y1)!=None ])
                  )
                 for y1 in y ]
        rank=sorted(TOPlist,key=operator.itemgetter(1),reverse=1)
        recommend=rank[0:self.topk]
        return recommend

    # 计算相似度（基于欧式距离的）
    def 欧式距离(self):
        distance = {}
        x,_=self.houxuanren()
        for a in x:
            dis = math.sqrt(sum([pow(float(self.sample[a][i]) - float(self.sample[self.name][i]), 2) for i in self.sample[self.name].keys()]))
            distance[a]=dis
        sortdistance=sorted(distance,key=operator.itemgetter(1))
        return distance
    #基于皮尔森相关性的相似度,待补充
    def person(self):
        return 1

def opensource(a):
  dic={}
  l=set()
  for line in open(a,encoding='utf-8-sig'):
     arr=line.strip().split(',')
     if len(arr)==3:
       dic.setdefault(arr[0],{})
       dic[arr[0]].setdefault(arr[1],{})
       dic[arr[0]][arr[1]]=arr[2]
  for i in dic.keys():
      b=set(dic[i].keys())
      l=l|b
  max=len(l)
  return len(dic),max,l,dic


if __name__ == '__main__':
   num,max,l,dic=opensource('resource.txt')
   print('记录人数：%d' %(num))
   print('共涉及电影数：%d' %(max))
   dk=recommendation(dic,'小花')
   print(dk.recommend())


