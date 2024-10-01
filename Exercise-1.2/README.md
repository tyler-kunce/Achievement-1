# Exercise 1.2

## Learning Goals
- Explain variables and data types in Python
- Summarize the user of objects in Python
- Create a data structure for your Recipe app

## Task Step 1
I will use a dictionary structure to store recipe details. One of the main
reasons for opting with dictionary is that it provides the ability to define
a key:value relationship which will be advantageous for the name, cooking_time,
and ingredients keys. Lastly, dictionary allows for modification, so if the
recipe needs to be edited later, dictionary provides that capability.

## Task Step 3
I will use a list structure for the all_recipes. Considering the requirement of
the structure be that it is "sequential in nature", list makes sense as it is an
ordered structure and allows for sorting.

## Journal
1. Imagine you’re having a conversation with a future colleague about whether to use the iPython Shell instead of Python’s default shell. What reasons would you give to explain the benefits of using the iPython Shell over the default one?

- iPython Shell offers a REPL that allows developers an environment featuring highlighting, tab completion functions, as well as the ability to test whole scripts of code.

2.	Python has a host of different data types that allow you to store and organize information. List 4 examples of data types that Python recognizes, briefly define them, and indicate whether they are scalar or non-scalar.

| Data type | Definition | Scalar or Non-Scalar |
| int | Represents integers, both negative and non-negative | Scalar |
| bool | Stores data of two types - True or False | Scalar |
| Tuples | Linear arrays that can store multiple values of any data type, immutable | Non-Scalar |
| Dictionaries | Structure for storing values and objects indexed by indentifiers known as keys | Non-Scalar |

3.	A frequent question at job interviews for Python developers is: what is the difference between lists and tuples in Python? Write down how you would respond.

- Probably the biggest difference between lists and tuples is the ability to modify. Tuples are considered immutable or non-modifiable while lists can be modified.

4.	In the task for this Exercise, you decided what you thought was the most suitable data structure for storing all the information for a recipe. Now, imagine you’re creating a language-learning app that helps users memorize vocabulary through flashcards. Users can input vocabulary words, definitions, and their category (noun, verb, etc.) into the flashcards. They can then quiz themselves by flipping through the flashcards. Think about the necessary data types and what would be the most suitable data structure for this language-learning app. Between tuples, lists, and dictionaries, which would you choose? Think about their respective advantages and limitations, and where flexibility might be useful if you were to continue developing the language-learning app beyond vocabulary memorization. 

- My preference or recommendation would be to use dictionaries as they offer the greatest flexibility and diversity for what data can be stored. Furthermore, they allow for edits and can be built upon, so could offer options for future enhancements or optimization.