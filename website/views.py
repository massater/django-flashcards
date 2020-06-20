from django.shortcuts import render
from random import randint

# Create your views here.
def home(request):
    return render(request, 'website/home.html', {})

def code(request):
    return render(request, 'website/code.html', {})

def add(request):
    num1 = randint(0, 10)
    num2 = randint(0, 10)
    if request.method == 'POST':
        answer = request.POST['answer']
        old_num1 = request.POST['old_num1']
        old_num2 = request.POST['old_num2']
        print(answer)

        # Error handling - no form filled out
        if not answer:
            my_answer = 'You forgot to fill out the form'
            color = 'warning'
            return render(request, 'website/add.html', {
                'answer': answer,
                'my_answer': my_answer,
                'num1': num1,
                'num2': num2,
                'color': color,
            })

        correct_answer = int(old_num1) + int(old_num2)
        if int(answer )== correct_answer:
            my_answer = "Correct! " + old_num1 + " + " + old_num2 + " = " + answer
            color = "success"
        else:
            color = "danger"
            my_answer = "Incorrect! " + old_num1 + " + " + old_num2 + " is not " + answer + "! It is " + str(correct_answer)

        return render(request, 'website/add.html', {
            'answer': answer,
            'my_answer': my_answer,
            'num1': num1,
            'num2': num2,
            'color': color,
        })

    return render(request, 'website/add.html', {
        'num1': num1,
        'num2': num2,
    })

def subtract(request):
    num1 = randint(0, 10)
    num2 = randint(0, 10)
    if request.method == 'POST':
        answer = request.POST['answer']
        old_num1 = request.POST['old_num1']
        old_num2 = request.POST['old_num2']
        print(answer)

        # Error handling - no form filled out
        if not answer:
            my_answer = 'You forgot to fill out the form'
            color = 'warning'
            return render(request, 'website/subtract.html', {
                'answer': answer,
                'my_answer': my_answer,
                'num1': num1,
                'num2': num2,
                'color': color,
            })

        correct_answer = int(old_num1) - int(old_num2)
        if int(answer) == correct_answer:
            my_answer = "Correct! " + old_num1 + " - " + old_num2 + " = " + answer
            color = "success"
        else:
            color = "danger"
            my_answer = "Incorrect! " + old_num1 + " - " + old_num2 + " is not " + answer + "! It is " + str(
                correct_answer)

        return render(request, 'website/subtract.html', {
            'answer': answer,
            'my_answer': my_answer,
            'num1': num1,
            'num2': num2,
            'color': color,
        })

    return render(request, 'website/subtract.html', {
        'num1': num1,
        'num2': num2,
    })

def multiple(request):
    num1 = randint(0, 10)
    num2 = randint(0, 10)
    if request.method == 'POST':
        answer = request.POST['answer']
        old_num1 = request.POST['old_num1']
        old_num2 = request.POST['old_num2']
        print(answer)
        # Error handling - no form filled out
        if not answer:
            my_answer = 'You forgot to fill out the form'
            color = 'warning'
            return render(request, 'website/multiply.html', {
                'answer': answer,
                'my_answer': my_answer,
                'num1': num1,
                'num2': num2,
                'color': color,
            })
        correct_answer = int(old_num1) * int(old_num2)
        if int(answer) == correct_answer:
            my_answer = "Correct! " + old_num1 + " x " + old_num2 + " = " + answer
            color = "success"
        else:
            color = "danger"
            my_answer = "Incorrect! " + old_num1 + " x " + old_num2 + " is not " + answer + "! It is " + str(
                correct_answer)

        return render(request, 'website/multiply.html', {
            'answer': answer,
            'my_answer': my_answer,
            'num1': num1,
            'num2': num2,
            'color': color,
        })

    return render(request, 'website/multiply.html', {
        'num1': num1,
        'num2': num2,
    })

def divide(request):
    num1 = randint(0, 10)
    num2 = randint(1, 10)
    if request.method == 'POST':
        answer = request.POST['answer']
        old_num1 = request.POST['old_num1']
        old_num2 = request.POST['old_num2']
        print(answer)

        correct_answer = int(old_num1) * int(old_num2)
        # Error handling - no form filled out
        if not answer:
            my_answer = 'You forgot to fill out the form'
            color = 'warning'
            return render(request, 'website/divide.html', {
            'answer': answer,
            'my_answer': my_answer,
            'num1': num1,
            'num2': num2,
            'color': color,
            })
        if float(answer) == correct_answer:
            my_answer = "Correct! " + old_num1 + " x " + old_num2 + " = " + answer
            color = "success"
        else:
            color = "danger"
            my_answer = "Incorrect! " + old_num1 + " x " + old_num2 + " is not " + answer + "! It is " + str(
                correct_answer)

        return render(request, 'website/divide.html', {
            'answer': answer,
            'my_answer': my_answer,
            'num1': num1,
            'num2': num2,
            'color': color,
        })

    return render(request, 'website/divide.html', {
        'num1': num1,
        'num2': num2,
    })