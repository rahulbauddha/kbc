
# question_list = [
# "1. How many continents are there?",
# "2. What is the capital of India?","3. NG mei kaun se course padhaya jaata hai?","4. who is the current odi captain of team india?","5. who is richest men in world?","6. who is miss universe of 2022?","7. how many gold medals india won in 2022 CWG?","8. who is vice president of india?"]

# options_list = [["1. Four", "2. Nine", "3. Seven", "4. Eight","5. lifeline"],["1. Chandigarh", "2. Bhopal", "3. Chennai", "4. Delhi","5. lifeline"],["1. Software Engineering", "2. Counseling", "3. Tourism", "4. Agriculture","5. lifeline"],["1. m.s.dhoni","2.rohit sharma","3.virat kohli","4.rishabh pant","5. lifeline"],["1. jeff bejos","2. bill gates","3.gautam adani","4. elon musk","5. lifeline"],["1.harnaj sindhu","2.harshika thakur","3.karoline","4.shree sashi","5. lifeline"],["1. 23","2. 18","3. 26","4. 22","5. lifeline"],["1. sudesh dhankar","2.jagdeep dhankar","3. draupadi murmu","4. nikhat zareen","5. lifeline"]]
# helpline_50_50=[["1. Nine","2. Seven"],["1. Chennai","2. Delhi"],["1. software engineering","2. counsiling"],["1.rohit sharma","2.virat kohli"],["1.gautam adani","2. elon musk"],["1.harnaj sindhu","2.harshika thakur"],["1. 23","2. 22"],["1.jagdeep dhankar","2. draupadi murmu",]]

# solution_list = [3, 4, 1, 2, 4, 2, 4, 2]
# helpline_sol=[2,2,1,1,2,2,2,1]
# phone_sol=[3,4,1,2,4,2,4,2]

# lifeline=["1. phone a friend","2. 50-50","3. audience poll","4. skeep the question"]

# color_list=["\033[1;32;40m","\033[1;33;40m","\033[1;34;40m","\033[1;35;40m","\033[1;36;40m","\033[1;32;40m","\033[1;33;40m","\033[1;34;40m","\033[1;35;40m","\033[1;36;40m"]
# price_c = 0
# price=[1000,2000,3000,4000,5000,6000,7000,8000]

# for x in range(len(question_list)):
#     print(f"aapka sawal hai\n{color_list[0]}\n{question_list[x]}\n{price[price_c]}$ ka\naapke options hai")
#     for j in options_list[x]:
#        print(f'{color_list[3]} {j}')
#     ans=int(input( f"{color_list[5]} enter your option.. "))
#     if ans==5:
#         for hp_li in lifeline:
#             print(hp_li)
#         ans1=int(input(f"{color_list[5]} enter your option.. "))
#         if ans1==1:
#             lifeline.pop(0)
#         elif ans1==2:
#             lifeline.pop(1)
#         elif ans1==3:
#             lifeline.pop(2)
#         else:
#             lifeline.pop(3)
#         if ans1==1:
#             print("you chose phone a friend")
#             ans=int(input( f"{color_list[5]} enter your answer.. "))
#             if ans==phone_sol[x]:
#                 print(color_list[2],"correct answer\n ",price [x])
#                 price_c+=1
#                 continue
#             else:
#                 print(color_list[2],"wrong answer")
#                 break
#         elif ans1==2:
#             print("you chose 50-50","\nyour options are",helpline_50_50[x])
#             ans=int(input("enter your answer.. "))
#             if ans==helpline_sol[x]:
#                 print(color_list[2],"correct answer\n ",price [x])
#                 price_c+=1
#                 continue
#             else:
#                 print(color_list[2],"wrong answer")
#                 break
#         elif ans1==4:
#             price_c+=0
#             continue
            
#     elif ans==solution_list[x]:
#        print(color_list[2],"correct answer\n ")
#        price_c+=1
#     else:
#        print(color_list[2],"wrong answer")

import matplotlib.pyplot as plt

bar= [["1. Four", "2. Nine", "3. Seven", "4. Eight",],["1. Chandigarh", "2. Bhopal", "3. Chennai", "4. Delhi"]]
bar_a=[[20,25,50,15],[5,15,25,55]]
New_Colors = ['green','blue','purple','brown']
plt.bar(bar[1], bar_a[1], color=New_Colors)
plt.title('audience response', fontsize=14)
plt.xlabel('polling', fontsize=14)
plt.ylabel('answers', fontsize=14)
plt.grid(True)
plt.show()