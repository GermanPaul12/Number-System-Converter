from tkinter import *
from tkinter import messagebox 
import customtkinter
from zahlensysteme import Zahlensysteme
import random

binary_nums = Zahlensysteme().list_generator('binary')
decimal_nums = [i for i in range(1, 1000)]
octal_nums = Zahlensysteme().list_generator('octal')
hex_nums = Zahlensysteme().list_generator('hex')

chosen_num = 0
random_input_num = 0
random_input_type = 'binary'
random_output_type = 'decimal'

root = customtkinter.CTk()

root.title('Number System Converter')

customtkinter.set_appearance_mode("System")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("blue")  # Themes: blue (default), dark-blue, green
root.geometry("1000x700")
root.configure(bg='black')


def convert_num():
  try:
    if input_type_combobox.get() == 'binary':
      if output_type_combobox.get() == 'decimal':
        result = Zahlensysteme().binary_to_decimal(num_entry.get())
        results_label.configure(text=f'The binary number {num_entry.get()} in decimal is {result}')  
        num_entry.delete(0, 'end')
      elif output_type_combobox.get() == 'hex':    
        result = Zahlensysteme().binary_to_hex(num_entry.get())
        results_label.configure(text=f'The binary number {num_entry.get()} in hex is {result}')  
        num_entry.delete(0, 'end')
      elif output_type_combobox.get() == 'octal':    
        result = Zahlensysteme().binary_to_octal(num_entry.get())
        results_label.configure(text=f'The binary number {num_entry.get()} in octal is {result}')  
        num_entry.delete(0, 'end')  
      else:
        result = num_entry.get()
        results_label.configure(text=f'The binary number {num_entry.get()} in binary is {result}')  
        num_entry.delete(0, 'end')    
        
        
    elif input_type_combobox.get() == 'decimal':
      if output_type_combobox.get() == 'binary':
        result = Zahlensysteme().decimal_to_binary(num_entry.get())
        results_label.configure(text=f'The decimal number {num_entry.get()} in binary is {result}')  
        num_entry.delete(0, 'end')
      elif output_type_combobox.get() == 'hex':    
        result = Zahlensysteme().decimal_to_hex(num_entry.get())
        results_label.configure(text=f'The decimal number {num_entry.get()} in hex is {result}')  
        num_entry.delete(0, 'end')
      elif output_type_combobox.get() == 'octal':    
        result = Zahlensysteme().decimal_to_octal(num_entry.get())
        results_label.configure(text=f'The decimal number {num_entry.get()} in octal is {result}')  
        num_entry.delete(0, 'end')  
      else:
        result = num_entry.get()
        results_label.configure(text=f'The decimal number {num_entry.get()} in decimal is {result}')  
        num_entry.delete(0, 'end')     
      
    elif input_type_combobox.get() == 'octal':
      if output_type_combobox.get() == 'binary':
        result = Zahlensysteme().octal_to_binary(num_entry.get())
        results_label.configure(text=f'The octal number {num_entry.get()} in binary is {result}')  
        num_entry.delete(0, 'end')
      elif output_type_combobox.get() == 'hex':    
        result = Zahlensysteme().octal_to_hexa(num_entry.get())
        results_label.configure(text=f'The octal number {num_entry.get()} in hex is {result}')  
        num_entry.delete(0, 'end')
      elif output_type_combobox.get() == 'decimal':    
        result = Zahlensysteme().octal_to_decimal(num_entry.get())
        results_label.configure(text=f'The octal number {num_entry.get()} in decimal is {result}')  
        num_entry.delete(0, 'end')  
      else:
        result = num_entry.get()
        results_label.configure(text=f'The octal number {num_entry.get()} in octal is {result}')  
        num_entry.delete(0, 'end')      
            
            
    elif input_type_combobox.get() == 'hex':
      if output_type_combobox.get() == 'binary':
        result = Zahlensysteme().hex_to_binary(num_entry.get())
        results_label.configure(text=f'The hex number {num_entry.get()} in binary is {result}')  
        num_entry.delete(0, 'end')
      elif output_type_combobox.get() == 'octal':    
        result = Zahlensysteme().hex_to_octal(num_entry.get())
        results_label.configure(text=f'The hex number {num_entry.get()} in octal is {result}')  
        num_entry.delete(0, 'end')
      elif output_type_combobox.get() == 'decimal':    
        result = Zahlensysteme().hex_to_decimal(num_entry.get())
        results_label.configure(text=f'The hex number {num_entry.get()} in decimal is {result}')  
        num_entry.delete(0, 'end')  
      else:
        result = num_entry.get()
        results_label.configure(text=f'The hex number {num_entry.get()} in hex is {result}')  
        num_entry.delete(0, 'end')   
        
                
  except Exception as e:
    messagebox.showerror(title='Error', message=e)    


def random_exercise():
  global chosen_num
  global random_input_type
  global random_output_type
  global random_input_num
  random_type_list = ['binary', 'hex', 'octal', 'decimal']
  random_input_type = random.choice(random_type_list)
  random_output_type = random.choice(random_type_list)
  while True:
    if random_input_type == random_output_type:
      random_output_type = random.choice(random_type_list)
    else:
      break
    
  if random_input_type == 'binary':
    random_input_num = random.choice(binary_nums)   
  elif random_input_type == 'hex':
    random_input_num = random.choice(hex_nums)      
  elif random_input_type == 'octal':
    random_input_num = random.choice(octal_nums)   
  else:
    random_input_num = random.choice(decimal_nums)    
  
  if random_input_type == 'binary':
    if random_output_type == 'decimal':
      result = Zahlensysteme().binary_to_decimal(random_input_num)
      exercises_label.configure(text=f'What is the binary number {random_input_num} in decimal:')
      exercise_entry.configure(fg_color='#2a9d8f')  
      
    elif random_output_type == 'hex':    
      result = Zahlensysteme().binary_to_hex(random_input_num)
      exercises_label.configure(text=f'What is the binary number {random_input_num} in hex: ')
      exercise_entry.configure(fg_color='#2a9d8f')  
      
    elif random_output_type == 'octal':    
      result = Zahlensysteme().binary_to_octal(random_input_num)
      exercises_label.configure(text=f'What is the binary number {random_input_num} in octal: ')
      exercise_entry.configure(fg_color='#2a9d8f')  
        
    else:
      result = random_input_num
      exercises_label.configure(text=f'What is the binary number {random_input_num} in binary: ')
      exercise_entry.configure(fg_color='#2a9d8f')  
          
        
  elif random_input_type == 'decimal':
    if random_output_type == 'binary':
      result = Zahlensysteme().decimal_to_binary(random_input_num)
      exercises_label.configure(text=f'What is the decimal number {random_input_num} in binary: ')
      exercise_entry.configure(fg_color='#2a9d8f')  
      
    elif random_output_type == 'hex':    
      result = Zahlensysteme().decimal_to_hex(random_input_num)
      exercises_label.configure(text=f'What is the decimal number {random_input_num} in hex: ')
      exercise_entry.configure(fg_color='#2a9d8f')  
      
    elif random_output_type == 'octal':    
      result = Zahlensysteme().decimal_to_octal(random_input_num)
      exercises_label.configure(text=f'What is the decimal number {random_input_num} in octal: ')
      exercise_entry.configure(fg_color='#2a9d8f')  
        
    else:
      result = random_input_num
      exercises_label.configure(text=f'What is the decimal number {random_input_num} in decimal: ')
      exercise_entry.configure(fg_color='#2a9d8f')  
          
    
  elif random_input_type == 'octal':
    if random_output_type == 'binary':
      result = Zahlensysteme().octal_to_binary(random_input_num)
      exercises_label.configure(text=f'What is the octal number {random_input_num} in binary: ')
      exercise_entry.configure(fg_color='#2a9d8f')  
      
    elif random_output_type == 'hex':    
      result = Zahlensysteme().octal_to_hexa(random_input_num)
      exercises_label.configure(text=f'What is the octal number {random_input_num} in hex: ')
      exercise_entry.configure(fg_color='#2a9d8f')  
      
    elif random_output_type == 'decimal':    
      result = Zahlensysteme().octal_to_decimal(random_input_num)
      exercises_label.configure(text=f'What is the octal number {random_input_num} in decimal: ')
      exercise_entry.configure(fg_color='#2a9d8f')  
        
    else:
      result = random_input_num
      exercises_label.configure(text=f'What is the octal number {random_input_num} in octal: ')
      exercise_entry.configure(fg_color='#2a9d8f')  
          
  elif random_input_type == 'hex':
    if random_output_type == 'binary':
      result = Zahlensysteme().hex_to_binary(random_input_num)
      exercises_label.configure(text=f'What is the hex number {random_input_num} in binary: ')
      exercise_entry.configure(fg_color='#2a9d8f')  
      
    elif random_output_type == 'octal':    
      result = Zahlensysteme().hex_to_octal(random_input_num)
      exercises_label.configure(text=f'What is the hex number {random_input_num} in octal: ')
      exercise_entry.configure(fg_color='#2a9d8f')  
      
    elif random_output_type == 'decimal':    
      result = Zahlensysteme().hex_to_decimal(random_input_num)
      exercises_label.configure(text=f'What is the hex number {random_input_num} in decimal: ')
      exercise_entry.configure(fg_color='#2a9d8f')  
        
    else:
      result = random_input_num
      exercises_label.configure(text=f'What is the hex number {random_input_num} in hex: ')
      exercise_entry.configure(fg_color='#2a9d8f')          
  chosen_num = result



def check_if_right():
  global chosen_num
  global random_input_type
  global random_output_type
  global random_input_num
  if str(chosen_num) == exercise_entry.get():
    with open('/Users/german/Documents/Coding/Python projects/DHBW/Zahlensysteme/log.csv', 'a+') as f:
      f.write(f"{random_input_type},{random_output_type},{random_input_num},{exercise_entry.get()},{chosen_num}\n")
    exercise_entry.configure(fg_color='green')
    exercise_entry.delete(0, 'end')
    messagebox.showinfo(title="Valid", message="Congrats you did it!")
    
    random_exercise()
  else:
    with open('/Users/german/Documents/Coding/Python projects/DHBW/Zahlensysteme/log.csv', 'a+') as f:
      f.write(f"{random_input_type},{random_output_type},{random_input_num},{exercise_entry.get()},{chosen_num}\n")
    exercise_entry.configure(fg_color='red')
    exercise_entry.delete(0, 'end')
    messagebox.showinfo(title="Not Valid", message="Sorry, but you're answer is not correct")
    
      
frame = customtkinter.CTkFrame(master=root,
                               width=1000,
                               height=700,
                               corner_radius=10,
                               bg='black',
                               fg_color='black',
                               border_width=2, border_color="white")





title_label = customtkinter.CTkLabel(root, text="Number System Converter", width=130,
                               height=40,
                               fg_color=("#2a9d8f", "#0F3D3E"),
                               corner_radius=8, 
                               text_font=('Times New Roman', 24),
                               bg_color='black',
                               )


input_type_label = customtkinter.CTkLabel(root, text="Input Type:", width=130,
                               height=40,
                               fg_color=("#2a9d8f", "#0F3D3E"),
                               corner_radius=8, 
                               text_font=('Times New Roman', 24),
                               bg_color='black',
                               )
input_type_combobox = customtkinter.CTkOptionMenu(master=root,
                                       values=['binary', 'octal', 'decimal', 'hex'], 
                                       width=80,
                                        height=40,
                                        fg_color=("#2a9d8f", "#0F3D3E"),
                                        corner_radius=8, 
                                        text_font=('Times New Roman', 24),
                                        bg_color='black',
                                        text_color='white',
                                        
                                        button_color='#0F3D3E',
                                        button_hover_color='#3AB4F2',
                                        dropdown_text_font=('Times New Roman', 24),
                                                           
                                        )

output_type_label = customtkinter.CTkLabel(root, text="Output Type:", width=130,
                               height=40,
                               fg_color=("#2a9d8f", "#0F3D3E"),
                               corner_radius=8, 
                               text_font=('Times New Roman', 24),
                               bg_color='black',
                               )
output_type_combobox = customtkinter.CTkOptionMenu(master=root,
                                       values=['binary', 'octal', 'decimal', 'hex'], 
                                       width=80,
                                        height=40,
                                        fg_color=("#2a9d8f", "#0F3D3E"),
                                        corner_radius=8, 
                                        text_font=('Times New Roman', 24),
                                        bg_color='black',
                                        text_color='white',
                                        
                                        button_color='#0F3D3E',
                                        button_hover_color='#3AB4F2',
                                        dropdown_text_font=('Times New Roman', 24),
                                                           
                                        )



convert_num_button = customtkinter.CTkButton(root, width=195,
                                 height=40,
                                 corner_radius=8,
                                 command=convert_num,
                                 text="Convert Num",
                                 fg_color='#2a9d8f',
                                 text_font=('Times New Roman', 24),
                               bg_color='black',
                               hover_color='#3AB4F2',
                               border_width=2, border_color="white",
                               text_color='black'
                                 )


num_label = customtkinter.CTkLabel(root, text="Input your number:", width=130,
                               height=40,
                               fg_color=("#2a9d8f", "#0F3D3E"),
                               corner_radius=8, 
                               text_font=('Times New Roman', 24),
                               bg_color='black',
                               )



num_entry = customtkinter.CTkEntry(root, width=140,
                               height=40,
                               corner_radius=10,
                              fg_color='#2a9d8f',
                              fg='white',
                              text_font=('Times New Roman', 20),
                              justify=CENTER,
                              bg_color='black',
                              border_width=2, border_color="white",
                              text_color='black'
                            )


results_label = customtkinter.CTkLabel(root, text="", width=130,
                               height=40,
                               fg_color=("#2a9d8f", "#0F3D3E"),
                               corner_radius=8, 
                               text_font=('Times New Roman', 24),
                               bg_color='black',
                               )


exercise_title_label = customtkinter.CTkLabel(root, text="Exercise Generator", width=130,
                               height=40,
                               fg_color=("#2a9d8f", "#0F3D3E"),
                               corner_radius=8, 
                               text_font=('Times New Roman', 24),
                               bg_color='black',
                               )

exercises_label = customtkinter.CTkLabel(root, text="", width=130,
                               height=40,
                               fg_color=("#2a9d8f", "#0F3D3E"),
                               corner_radius=8, 
                               text_font=('Times New Roman', 24),
                               bg_color='black',
                               )

exercise_entry = customtkinter.CTkEntry(root, width=140,
                               height=40,
                               corner_radius=10,
                              fg_color='#2a9d8f',
                              fg='white',
                              text_font=('Times New Roman', 20),
                              justify=CENTER,
                              bg_color='black',
                              border_width=2, border_color="white",
                              text_color='black'
                            )


new_exercise_button = customtkinter.CTkButton(root, width=195,
                                 height=40,
                                 corner_radius=8,
                                 command=random_exercise,
                                 text="Generate New Exercise",
                                 fg_color='#2a9d8f',
                                 text_font=('Times New Roman', 24),
                               bg_color='black',
                               hover_color='#3AB4F2',
                               border_width=2, border_color="white",
                               text_color='black'
                                 )

check_exercise_button = customtkinter.CTkButton(root, width=195,
                                 height=40,
                                 corner_radius=8,
                                 command=check_if_right,
                                 text="Check if you calculated right",
                                 fg_color='#2a9d8f',
                                 text_font=('Times New Roman', 24),
                               bg_color='black',
                               hover_color='#3AB4F2',
                               border_width=2, border_color="white",
                               text_color='black'
                                 )

random_exercise()

#Packing them on the screen
frame.grid(row=0, column=0, columnspan=6, rowspan=8, sticky='news')

title_label.grid(row=0, column=0, columnspan=6, sticky='ew', padx=10, rowspan=1)

input_type_label.grid(row=1, column=0, columnspan=2, rowspan=1, sticky='ew', padx=10)
input_type_combobox.grid(row=1, column=2, columnspan=2, rowspan=1, sticky='ew', padx=10)
input_type_combobox.set('decimal')

output_type_label.grid(row=2, column=0, columnspan=2, rowspan=1, sticky='ew', padx=10)
output_type_combobox.grid(row=2, column=2, columnspan=2, rowspan=1, sticky='ew', padx=10)
output_type_combobox.set('binary')

results_label.grid(row=4, column=0, columnspan=6, sticky='ew', padx=10, rowspan=1)

convert_num_button.grid(row=1, column=4, columnspan=2, sticky='nsew', padx=10, rowspan=3, pady=30)

num_label.grid(row=3, column=0, columnspan=2, sticky='ew', padx=10, rowspan=1) 
num_entry.grid(row=3, column=2, columnspan=2, sticky='ew', padx=10, rowspan=1)   

exercise_title_label.grid(row=5, column=0, columnspan=6, sticky='ew', padx=10, rowspan=1)

exercises_label.grid(row=6, column=0, columnspan=3, sticky='ew', padx=10, rowspan=1)
exercise_entry.grid(row=6, column=3, columnspan=3, sticky='ew', padx=10, rowspan=1)

new_exercise_button.grid(row=7, column=0, columnspan=3, sticky='ew', padx=10, rowspan=1)
check_exercise_button.grid(row=7, column=3, columnspan=3, sticky='ew', padx=10, rowspan=1)

root.mainloop()