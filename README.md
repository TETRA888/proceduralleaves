# This is basic Blender-Python script that creates a maple mesh leave

# My initial idea was to manually plot out the location of the vertices of the leaf:
![background](https://github.com/user-attachments/assets/da9021cf-bf34-4782-a735-8abe8ab81903)
## However, I quickly realized how tedious and inefficient this implementation would be. Additionally, since I want to make different sized leaves, It would be difficult to properly adjust the location of the vertices without introducing some obfuscated method

# Here is my second idea that just simply involved using a parametric equation that was provided by ChatGPT I just appended the x and y coordinates that were scaled using a parameter I created called LOD (Level Of Detail)
![image](https://github.com/user-attachments/assets/e939be1f-4190-47c3-96b8-754a9231ed74)

# Here is a set of generated leaves that I made by randomly adjusting certain parameters in the parametric equation:
![image](https://github.com/user-attachments/assets/37ddb718-895d-40c7-bc10-4bb29fcba122)

# Here is me generating a patch of leaves using a simple for loop:
![image](https://github.com/user-attachments/assets/0f8e1c4a-c21a-4d8f-bd66-6e3a5ef7fbf0)

# And after adding some color ranges I get this nice clean patch:
![image](https://github.com/user-attachments/assets/65a3e3bf-7ecd-42a6-a2d1-0e91c2223541)

# Adjusting some of the parameters I can get different results:
![image](https://github.com/user-attachments/assets/b78ded78-b57e-43d0-a93e-671b1add5e95)

