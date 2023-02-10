# polymorphism with inheritance


"""
JAVA

public static func(a){

}

public static func(a, b){
    
}

public static func(a, b, c){
    
}

"""

class Bird:

    def fly(self):
        print("i am flying.")

class Parrot(Bird):
    
    # override
    def fly(self):
        print("Parrot is flying.")
    
class Panguin(Bird):
    
    def fly(self):
        print("Panguin can't fly.")
