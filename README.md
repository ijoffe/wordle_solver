# Wordle Solver v3

## Table of Contents
* [General Information](#general-information)
* [Description](#description)
* [Background](#background)
* [Results](#results)
* [Technologies](#technologies)
* [Instructions](#instructions)
* [Example Usage](#example-usage)

## General Information
This repository contains code to solve the popular game Wordle. Some folders in this repository contain previous iterations of the algorithm, but the best and most recent implementation is contained in the main directory. All code was created by me, Isaac Joffe, in February of 2022.

## Description
The aim of this project is to create an algorithm that can successfully find the correct word in the game Wordle within the given number of attempts in all cases. This repository contains an algorithm that can successfully determine all words, and the vast majority within enough attempts.

The algorithm works by choosing the words that are able to eliminate the most letters at once until the set of all potentially correct words is small enough to guess for correctness.

## Background
Wordle is a widely popular puzzle game similar to the common board game Mastermind. The game involves using six guesses to try to determine a daily secret word. More information about the game's history and mechanics can be found at the following link: https://en.wikipedia.org/wiki/Wordle. The game can be played at the following link: https://www.nytimes.com/games/wordle/index.html.

When Wordle rapidly became very popluar in late 2021 and early 2022, I often struggled to correctly and efficiently solve the puzzles compared to my friends and family. After continually getting lower scores, I decided to create an algorithm that could beat most people at the game.

## Results
By creating a version of the Wordle algorithm itself, I was able to run mass testing to determine the general efficiency and accuracy of my algorithm. 

When testing over all possibly correct Wordle words and guessing only from the same set (achieved by running `python3 wordle_test.py test_words.txt test_words.txt`), I found that 99.7% of all words were solved within six attempts (only eight words could not be solved fast enough), with an average of only 3.7 attempts required.

When testing over all possibly correct Wordle words and guessing from all valid Wordle words (achieved by running `python3 wordle_test.py test_words.txt words.txt`), I found that 94.5% of all words were solved within six attempts, with an average of 4.4 attempts being required.

When testing over all valid Wordle words and guessing from all valid Wordle words (achieved by running `python3 wordle_test.py words.txt words.txt`), I found that 91.2% of all words were solved within six attempts, with an average of 4.6 attempts being required.

## Technologies
All code contained is written in Python 3.8.10. I created all the code and files in this repository using my personal virtual machine, which runs the Ubuntu distribution of the Linux operating system, through the Sublime Text text editor and the Linux terminal window.

## Instructions
Currently, the program can only be used directly through a terminal window. To guess Wordle's daily word, there are two choices of programs that can be run. To guess based off of the set of all valid words that Wordle will accept as input, simply run `python3 wordle_solver.py words.txt` in a terminal window. To guess off of the set of all potentially correct words that may actually be Wordle's word of the day, simply run `python3 wordle_solver.py test_words.txt` in a terminal window. While the second choice generally determines the correct word faster and in less attempts, there is a small chance that the instance mnay not be solvable if new words have been added. Now, begin entering the suggested words into the Wordle website and enter the result that wordle gives ('b' for a black/white letter, 'y' for a yellow letter, and 'g' for a green letter) in the order given into the terminal until the program guesses the correct word.

## Example Usage
For the command `python3 wordle_solver.py words.txt`:
```
Now try: aeros
Enter result: yybby
Now try: plant
Enter result: gbybb
Now try: paise
Enter result: ggbgg
Now try: pause
Enter result: ggggg
```
And for the command `python3 wordle_solver.py test_words.txt`:
```
Now try: alert
Enter result: ybybb
Now try: shuck
Enter result: ybgbb
Now try: pause
Enter result: ggggg
```
