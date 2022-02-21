# Wordle Solver v2

## Table of Contents
* [General Information](#general-information)
* [Description](#description)
* [Background](#background)
* [Technologies](#technologies)
* [Instructions](#instructions)
* [Example Usage](#example-usage)

## General Information
This subdirectory contains the second version of code to solve the popular game Wordle. All code was created by me, Isaac Joffe, in February of 2022.

## Description
The aim of this project is to create an algorithm that can successfully find the correct word in the game Wordle within the given number of attempts in all cases. This subdirectory of the repository contains an algorithm that can successfully determine all words, and mostly in enough attempts (although it falters in some specfic cases).

While the code contained solves previous issues including double-letter glitches and optimization problems, there is still room for improvement. The current algorithm is a greedy algorithm - each turn it always tries to guess the correct word, without regard to guessing the correct word in the least number of tries. This improves the previous algorithm in many cases but falters for some words (for example, "taxes" - the algorithm takes nine tries since many words have a similar structures and 'x' is an uncommon letter).

## Background
Wordle is a widely popular puzzle game similar to the common board game Mastermind. The game involves using six guesses to try to determine a daily secret word. More information about the game's history and mechanics can be found at the following link: https://en.wikipedia.org/wiki/Wordle. The game can be played at the following link: https://www.nytimes.com/games/wordle/index.html.

When Wordle rapidly became very popluar in late 2021 and early 2022, I often struggled to correctly and efficiently solve the puzzles compared to my friends and family. After continually getting lower scores, I decided to create an algorithm that could beat most people at the game.

## Technologies
All code contained is written in Python 3.8.10. I created all the code and files in this repository using my personal virtual machine, which runs the Ubuntu distribution of the Linux operating system, through the Sublime Text text editor and the Linux terminal window.

## Instructions
Currently, the program can only be used directly through a terminal window. To run the program, first enter `python3 word_processor.py all_words.txt`, and then simply enter `python3 wordle_solver.py all_word.txt.pkl` in the terminal. Now, begin entering the suggested words into the Wordle website and enter the result that wordle gives ('b' for a black/white letter, 'y' for a yellow letter, and 'g' for a green letter) in the order given into the terminal until the program guesses the correct word.

## Example Usage
```
Number of possible words: 12966
Now try: aeros
Enter result: yybby
Number of possible words: 129
Now try: isnae
Enter result: bybyg
Number of possible words: 65
Now try: slate
Enter result: ybybg
Number of possible words: 10
Now try: cause
Enter result: bgggg
Number of possible words: 2
Now try: pause
Enter result: ggggg
```
