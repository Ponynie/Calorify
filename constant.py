from torchvision import transforms

transform = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.ToTensor(),
    transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])
])

food_list = [('French Fries', '20 kcal/piece'),
             ('Fried Chicken', '345 kcal/piece'), 
             ('Grilled Chicken', '165 kcal/piece'), 
             ('Green Curry', '240 kcal'), 
             ('Hamburger', '245 kcal/piece'), 
             ('Omelette', '215 kcal'), 
             ('Chicken Biryani', '534 kcal'), 
             ('Krapao Crispy Pork', '650 kcal'), 
             ('Krapao Crispy Pork with Fried Egg', '865 kcal'), 
             ('Krapao Minced Pork', '580 kcal'), 
             ('Krapao Minced Pork with Fried Egg', '795 kcal'), 
             ('Mango Sticky Rice', '450 kcal'), 
             ('Stir-fried Rice Noodles with Soy Sauce and Pork', '679 kcal'), 
             ('Pad Thai', '545 kcal'), 
             ('Pizza', '266 kcal/100 g'), 
             ('Papaya Salad', '120 kcal'), 
             ('Tom Kha', '210 kcal'), 
             ('Tom Yum', '65 kcal')]