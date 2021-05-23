import math
import random

"""
Create sequences of numbers.

Format:
function(amount, start, max_, truncated)

Default values:
function(amount=100, start=0, max_=100, truncated=True)
function(amount=100, start=0, max_=100, truncated=True)
"""

def pair_equal(amount=100, start=0, stop=100, truncated=True):
    """
    Returns a dictionary in which the values of each pair are equal.
    """
    sequence = []
    amount = amount + start


    for x in range(start, amount):
        if truncated and x >= stop:
            sequence.append(stop)
        else:
            sequence.append(x)

    return sequence

def random_sequence(amount=100, start=0, stop=0, reverse=False):
    """
    Returns a sequence of a specified number of elements between two given values.
    If it receives the reverse=True parameter, it returns the sequence in reverse order of the received values.
    """
    
    sequence = []
    if start == stop:
        for i in range(amount):
            sequence.append(stop)
    elif start < stop and not reverse: 
        for i in range(amount):
            number = random.randrange(start, stop)
            sequence.append(number)
        sequence.sort()
    elif start < stop and reverse: 
        for i in range(amount):
            number = random.randrange(start, stop)
            sequence.append(number)
        sequence.sort(reverse=True)

    elif start > stop and not reverse: 
        for i in range(amount):
            number = random.randrange(stop, start)
            sequence.append(number)
        sequence.sort()
    elif start > stop and reverse: 
        for i in range(amount):
            number = random.randrange(stop, start)
            sequence.append(number)
        sequence.sort(reverse=True)
    return sequence

def create_sequence(function):
    def wrapper(amount=100, start=0, stop=0, truncated=False, ordered=False):
        """
        Decorate the sequencing funcions
        """
        amount = amount + start
        sequence = []
        sequence = function(amount, start, stop, truncated, sequence)
        if ordered and ordered != 'reverse':
            sequence.sort()
        elif ordered:
            sequence.sort(reverse=True)
        return sequence

    return wrapper

@create_sequence
def cubes(amount, start, stop, truncated, sequence):
        """
        Returns a list with cubes.
        """
        for x in range(start, amount):
            y = x ** 3
            if truncated and y >= stop:
                sequence.append(stop)
            else:
                sequence.append(y)
        return sequence

@create_sequence
def squares(amount, start, stop, truncated, sequence):
        """
        Returns a list with squares.
        """
        for x in range(start, amount):
            y = x * x
            if truncated and y >= stop:
                sequence.append(stop)
            else:
                sequence.append(y)
        return sequence

    
@create_sequence
def sines(amount, start, stop, truncated, sequence):
        """
        Returns a list with sines.
        """

        for x in range(start, amount):
            y = abs(round(stop * math.sin(x)))
            if truncated and y >= stop:
                sequence.append(stop)
            elif y < start:
                sequence.append(start)
            else:
                sequence.append(y)
        return sequence

@create_sequence
def cosines(amount, start, stop, truncated, sequence):
        """
        Returns a list with cosines.
        """

        for x in range(start, amount):
            y = abs(round(stop * math.cos(x)))
            if truncated and y >= stop:
                sequence.append(stop)
            elif y < start:
                sequence.append(start)
            else:
                sequence.append(y)
        return sequence


@create_sequence
def tangents(amount, start, stop, truncated, sequence):
        """
        Returns a list with tangents.
        """

        for x in range(start, amount):
            y = abs(round(stop * math.tan(x)))
            if truncated and y >= stop:
                sequence.append(stop)
            elif y < start:
                sequence.append(start)
            else:
                sequence.append(y)
        return sequence


@create_sequence
def arc_tangents(amount, start, stop, truncated, sequence):
        """
        Returns a list with arc tangents.
        """
        ratio = (start + stop) / 2
        for x in range(start, amount):
            y = abs(round(ratio * math.atan(x)))
            if truncated and y >= stop:
                sequence.append(stop)
            elif y < start:
                sequence.append(start)
            else:
                sequence.append(y)
        return sequence

@create_sequence
def hypotes(amount, start, stop, truncated, sequence):
        """
        Returns a list with hypotes.
        """
        ratio = (start + stop) / 10
        for x in range(start, amount):
            y = abs(round(ratio * math.hypot(x, start)))
            if truncated and y >= stop:
                sequence.append(stop)
            elif y < start:
                sequence.append(start)
            else:
                sequence.append(y)
        return sequence

@create_sequence
def inverse_hyperbolic_sine(amount, start, stop, truncated, sequence):
        """
        Returns a list with inverse hiperbolic sines.
        """
        ratio = (start + stop) / 5
        for x in range(start, amount):
            y = abs(round(ratio * math.asinh(x)))
            if truncated and y >= stop:
                sequence.append(stop)
            elif y < start:
                sequence.append(start)
            else:
                sequence.append(y)
        return sequence

@create_sequence
def hyperbolic_sine(amount, start, stop, truncated, sequence):
        """
        Returns a list with hyperbolic sines.
        """
        ratio = 1
        for x in range(start, amount):
            y = abs(round(ratio * math.sinh(x)))
            if truncated and y >= stop:
                sequence.append(stop)
            elif y < start:
                sequence.append(start)
            else:
                sequence.append(y)
        return sequence


@create_sequence
def power_e(amount, start, stop, truncated, sequence):
        """
        Returns a list with powers.
        """
        ratio = .5
        for x in range(start, amount):
            y = abs(round(ratio * math.exp(x)))
            if truncated and y >= stop:
                sequence.append(stop)
            elif y < start:
                sequence.append(start)
            else:
                sequence.append(y)
        return sequence

@create_sequence
def power_em1(amount, start, stop, truncated, sequence):
        """
        Returns a list with powers.
        """
        ratio = .25
        for x in range(start, amount):
            y = abs(round(ratio * math.expm1(x)))
            if truncated and y >= stop:
                sequence.append(stop)
            elif y < start:
                sequence.append(start)
            else:
                sequence.append(y)
        return sequence

@create_sequence
def fraction(amount, start, stop, truncated, sequence):
        """
        Returns a list with fractions.
        """
        ratio = stop
        for x in range(start, amount):
            y = abs(round(ratio / (abs(x) + 1)))
            if truncated and y >= stop:
                sequence.append(stop)
            elif y < start:
                sequence.append(start)
            else:
                sequence.append(y)
        return sequence

@create_sequence
def log(amount, start, stop, truncated, sequence):
        """
        Returns a list with logarithms.
        """
        ratio = 10 ** (len(str(start)) + 1)
        for x in range(start, amount):
            # y = abs(round(math.log(x, 1)))
            y = abs(round(math.log1p(x) * ratio * 5))
            if truncated and y >= stop:
                sequence.append(stop)
            elif y < start:
                sequence.append(start)
            else:
                sequence.append(y)
        return sequence

@create_sequence
def power(amount, start, stop, truncated, sequence):
        """
        Returns a list with powers.
        """
        ratio = len(str(start)) + 1
        for x in range(start, amount):
            y = abs(round(ratio ** x))
            if truncated and y >= stop:
                sequence.append(stop)
            elif y < start:
                sequence.append(start)
            else:
                sequence.append(y)
        return sequence

def smoothed(sequence, step=1, start=0):
    """Insert intermediate elements into a number sequence."""
    next_index = start + 1
    last = len(sequence) 
    new_sequence = []
    if not step:
        return sequence
    ratio_step = step + 1
    for item in sequence:
        new_sequence.append(item)
        if next_index < last:
            next_item = sequence[next_index]
            ratio = (item + next_item) / (step + 1)
            ratio = int(ratio)
            for x in range(step):
                value = (ratio * x) + item
                new_sequence.append(int(value))
        next_index = next_index + 1
    return new_sequence
