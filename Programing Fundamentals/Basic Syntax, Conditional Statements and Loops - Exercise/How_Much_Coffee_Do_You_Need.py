# The list of events can contain the following:
#     • You have homework to do ("coding").
#     • You have a dog or a cat that decided to wake you up too early ("dog" or "cat").
#     • You watch a movie ("movie").
#     • If other events are present, they will be represented by arbitrary strings. Just ignore them!
# Each event can be lowercase or uppercase:
#     • If it is lowercase, you need 1 coffee by an event.
#     • If it is uppercase, you need 2 coffees by an event.
# In the end, print the number of coffees you will need. If the count has exceeded 5, just print "You need extra sleep".
coffee_counter = 0
while True:
    line = input()
    if line == "END":
        break

    if line == "coding" or line == "dog" or line == "cat" or line == "movie":
        coffee_counter += 1
    elif line == "CODING" or line == "DOG" or line == "CAT" or line == "MOVIE":
        coffee_counter += 2

if coffee_counter > 5:
    print("You need extra sleep")
else:
    print(coffee_counter)