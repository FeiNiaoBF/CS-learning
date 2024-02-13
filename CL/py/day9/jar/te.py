class MyClass:
    @classmethod
    def class_method(cls):
        print("This is a class method")

    @staticmethod
    def static_method():
        print("This is a static method")

# 调用类方法
MyClass.class_method()

# 调用静态方法
MyClass.static_method()
