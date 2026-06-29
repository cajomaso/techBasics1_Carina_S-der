### Template for Code Reading Exercise

1. Where did you find the code and why did you choose it? (Provide the link)

I found this code when I searched for pygame code that makes textboxes, because Text Boxes are necessary for my characters to talk.
Link: https://github.com/benedsmith/PyTextBox/tree/master

---

2. What does the program do? What's the general structure of the program? 

In the one file the class for creating text boxes is written. Giving some options to personalize the text box.
In the other one there is an example code that shows you how to make use of that class by creating two textboxes.


---

3. Function analysis: pick one function and analyze it in detail:

First the class is created. In the class enables you to change the look of your text box. It has parameters like the text, which is written later in the window, background color of the box, the text color, font and font size.

In the function draw it first draws the rectangle of the box. Then it checks if there is more than one letter to the given text(see second .py file).
with .render a new surface is being created, which shows the text.https://www.pygame.org/docs/ref/font.html

The function def text_input makes it able to write text into the boxes. First it checks if we press the backspace on the keyboard, which deletes the last letter. If enter or return is pressed. The color changes back and the box is no longer active.
Behind every letter there is a number with the last if-check the code only allows the input of letters.https://www.pygame.org/docs/ref/key.html

With def test_collide, it is being checked if we press the mouse button on one of the boxes. This determines if the box is active (FALSE/TRUE) and which background color the box should have.

It was also important for me to look at the usage_example.py so I can understand how I can handle the classes. It also helped me understand TextBox.py. It also gave me a slight inside how to easily get functions from a different file.




---

4. Takeaways: are there anything you can learn from the code? (How to structure your code, a clean solution for some function you might also need...)

I learned less structure-wise but more in terms how to implement text boxes in my very text-heavy game. I personally will try to add a background image instead of a background color.
It also showed me with def test_collide how I can check if a mouseclick is on a certain surface. This will be useful for interacting with characters.
I will probably not need def text_input.


5. What parts of the code were confusing or difficult at the beginning to understand?
- Were you able to understand what it is doing after your own research?
When I went through TextBox.py the first time I was confused because I thought information was missing, for example in def draw I asked myself from where python knows the text from self.text. But when I checked the example it made sense. The code also had some pygame modules I did not know before: e. g. .render() or the name of different inputs from the keyboard.
---

Extra notes
