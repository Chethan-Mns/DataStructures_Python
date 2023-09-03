# DataStructures_Python

This repository contains implementations of various data structures in Python. These data structures were practiced as part of my learning journey in the "Data Structures with Python" course on Udemy.

## Table of Contents

- [Introduction](#introduction)
- [Data Structures](#data-structures)
- [How to Use](#how-to-use)
- [Contributing](#contributing)
- [License](#license)

## Introduction

In this repository, you'll find Python implementations of fundamental data structures commonly used in computer science and software development. Each data structure is organized into its own module, making it easy to understand and use.

## Data Structures

Here are the data structures included in this repository:

- [Linked List](./linked_list.py)
- [Stack](./stack.py)
- [Queue](./queue.py)
- [Binary Search Tree](./BST.py)

Feel free to explore each data structure to learn more about their implementations.

## How to Use

To use any of the data structures in your own Python projects, simply import the corresponding module. For example, if you want to use the linked list implementation:

```python
from linked_list import LinkedList

# Create a new linked list
my_list = LinkedList()

# Perform operations on the linked list
my_list.append(42)
my_list.prepend(10)
my_list.delete(42)
