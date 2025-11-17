class Vehicle:
    """
    车辆类 - 用于表示各种类型的车辆
    
    这个类定义了车辆的基本属性和行为，包括品牌、型号、年份和速度等。
    可以作为其他具体车辆类型（如汽车、摩托车等）的基类。
    """
    
    def __init__(self, brand, model, year):
        """
        初始化车辆对象
        
        参数:
            brand (str): 车辆品牌，如"丰田"、"本田"等
            model (str): 车辆型号，如"卡罗拉"、"雅阁"等  
            year (int): 车辆生产年份
        """
        self.brand = brand      # 车辆品牌
        self.model = model      # 车辆型号
        self.year = year        # 生产年份
        self.speed = 0          # 当前速度，初始化为0
    
    def start_engine(self):
        """
        启动引擎方法
        
        返回:
            str: 引擎启动的提示信息
        """
        return f"{self.brand} {self.model} 的引擎启动了"
    
    def accelerate(self, increment=10):
        """
        加速方法 - 增加车辆速度
        
        参数:
            increment (int): 速度增量，默认为10km/h
            
        返回:
            str: 加速后的状态信息
        """
        self.speed += increment
        return f"{self.brand} {self.model} 加速到 {self.speed} km/h"
    
    def brake(self, decrement=10):
        """
        刹车方法 - 减少车辆速度
        
        参数:
            decrement (int): 速度减量，默认为10km/h
            
        返回:
            str: 刹车后的状态信息
        """
        self.speed = max(0, self.speed - decrement)  # 确保速度不会小于0
        return f"{self.brand} {self.model} 减速到 {self.speed} km/h"
    
    def get_info(self):
        """
        获取车辆详细信息
        
        返回:
            str: 包含车辆所有信息的字符串
        """
        return f"车辆信息: {self.year}年 {self.brand} {self.model}, 当前速度: {self.speed} km/h"
    
    def stop(self):
        """
        停车方法 - 将速度设为0
        
        返回:
            str: 停车状态信息
        """
        self.speed = 0
        return f"{self.brand} {self.model} 已停车"


# 使用示例
if __name__ == "__main__":
    # 创建一个车辆实例
    my_car = Vehicle("丰田", "卡罗拉", 2023)
    
    # 演示各种方法的使用
    print(my_car.get_info())           # 显示车辆信息
    print(my_car.start_engine())       # 启动引擎
    print(my_car.accelerate(20))       # 加速20km/h
    print(my_car.accelerate())         # 默认加速10km/h
    print(my_car.brake(15))            # 减速15km/h
    print(my_car.get_info())           # 显示当前状态
    print(my_car.stop())               # 停车