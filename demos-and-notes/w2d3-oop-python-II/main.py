# this function does not make widgets. it will create functions that DO create widgets
def WidgetMakerMaker(widget_color):

    def WidgetMaker():
        return {
            'type': 'widget',
            'color': widget_color,
        }
    
    return WidgetMaker

RedWidgetMaker = WidgetMakerMaker('red')
red_widget = RedWidgetMaker()
another_red_widget = RedWidgetMaker()

# print(RedWidgetMaker)
# print(red_widget)
# print(another_red_widget)

BlueWidgetMaker = WidgetMakerMaker('blue')
blue_widget = BlueWidgetMaker()
another_blue_widget = BlueWidgetMaker()

# print(blue_widget)
# print(another_blue_widget)


from datetime import datetime

def AddOne(num):
    return num + 1

def MultiplyByTwo(num):
    return num * 2



def PrintCurrentTimeAndAlso(func):
    def WrapperFunction(*args, **kwargs):

        print(f'Calling {func.__name__} at {datetime.now()}')

        output = func(*args, **kwargs)
    
        print(f'Calling {func.__name__} again at {datetime.now()}')
        return output

    return WrapperFunction

# we call our decorator function, passing in the function to be decorated, returning a decorated function
PrintCurrentTimeAndAlsoAddOne = PrintCurrentTimeAndAlso(AddOne)

# one_plus_one = PrintCurrentTimeAndAlsoAddOne(1)

# print(one_plus_one)

PrintCurrentTimeAndAlsoMultiplyByTwo = PrintCurrentTimeAndAlso(MultiplyByTwo)
# two_times_two = PrintCurrentTimeAndAlsoMultiplyByTwo(2)

# print(two_times_two)

@PrintCurrentTimeAndAlso
def SubtractThree(num):
    return num - 3

nine_minus_three = SubtractThree(9)
print(nine_minus_three)