# Exercise 1.4

## Learning Goals
- Use files to store and retrieve data in Python

## Journal
1.	Why is file storage important when you’re using Python? What would happen if you didn’t store local files?

- File storage allows for storage of data and code for future retrieval and use. If you didn't store this data, it would be wiped from memory when the script ends.

2.	In this Exercise you learned about the pickling process with the pickle.dump() method. What are pickles? In which situations would you choose to use pickles and why? 

- Pickles are complex data packaged into a stream of bytes readable by machines. Pickles are used when complex data structures need to be saved/stored that can't be handled by simpler text files.

3.	In Python, what function do you use to find out which directory you’re currently in? What if you wanted to change your current working directory?

- `os.getcwd()` is used to tell the user the current working directory. To change the current working directory, the user would utilize the `os.chdir()` with the desired directory path included in the parentheses.

4.	Imagine you’re working on a Python script and are worried there may be an error in a block of code. How would you approach the situation to prevent the entire script from terminating due to an error?

- I would use the `try-except-else-finally` blocks to ensure my code was checked for errors and properly routed.

5.	You’re now more than halfway through Achievement 1! Take a moment to reflect on your learning in the course so far. How is it going? What’s something you’re proud of so far? Is there something you’re struggling with? What do you need more practice with? Feel free to use these notes to guide your next mentor call. 

- I think my learning is going really well to this point. I'm especially proud of how I'm grasping concepts and methods throughout the exercises and the practice exercises. I do feel like it takes me some time to apply what I've learned and used throughout the exercise into the Achievement tasks. I often find myself having to refer back quite a bit to the sections and refresh myself on what was presented. I think I just need to take my time getting through the content and probably take better notes as well as not feel discouraged about having to read through two or three times more.