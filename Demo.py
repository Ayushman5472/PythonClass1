Score1 = int (input("Enter First Game score here:   "))
Score2 = int (input("Enter Second Game score here:   "))
Score3 = int (input("Enter Third Game score here:   "))
Score4 = int (input("Enter Fourth Game score here:   "))
Score5 = int (input("Enter Fifth Game score here:   "))

if(Score1<5):
    Score1=0

if(Score2<5):
    Score2=0

if(Score3<5):
    Score3=0

if(Score4<5):
    Score4=0

if(Score5<5):
    Score5=0

TotalScore = Score1 + Score2 + Score3 + Score4 + Score5

print(TotalScore)