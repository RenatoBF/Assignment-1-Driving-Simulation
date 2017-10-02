
initial_velocity = 0
time = int(input('Input Time:'))
acceleration = int(input('Input Acceleration:'))
distance = int(input('Input Distance:'))
speed_limit = 60

for i in range(time+1):
    velocity = int(initial_velocity + acceleration * i)
    distance1 = int(.5 * i * (velocity + initial_velocity))
    num = int(distance1 / 10)
    print('duration: ' + str(i) + " distance: " + "*" * num)

if velocity > speed_limit:
    print('The person went over the speed limit.Max speed was ' + str(velocity) + "s")
else:
    print('The person did not goover the speed limit.Max speed was ' + str(velocity) + "s")

if distance1 >= distance:
    print('The person reached the destination.Reached ' + str(distance1))
else:
    print('The person did not reach the destination.Reached ' + str(distance1))
