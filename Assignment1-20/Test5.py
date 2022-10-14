dic = {'23/07/2021' : ['Dance', 'Story telling'], '05/07/2021' : ['Singing', 'Cricket'], '11/04/2021' : ['Robo wars', 'Tug of wars']}
check = str(input("Enter the date "))
if check in dic :
    print("Occured events", dic[check])
    print()
else:
    print("No events occured on this date")