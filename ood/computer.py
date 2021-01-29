# 组装一台电脑

# CPU/RAM/Disk
class CPU(object):
    """
    CPU类
    """

    def __init__(self, brand, core, interface):
        self.brand = brand
        self.core = core
        self.interface = interface


class RAM(object):
    """
    内存条
    """

    def __init__(self, brand, size):
        self.brand = brand
        self.size = size


class Disk(object):
    """
    硬盘类
    """

    def __init__(self, brand, size):
        self.brand = brand
        self.size = size


class Computer(object):
    """
    电脑类
    """

    def __init__(self, cpu_interface, ram_count, disk_count):
        self.cpu_interface = cpu_interface
        self.ram_count = ram_count
        self.disk_count = disk_count

        # 以下三行是私有属性
        self.__cpu = None  # 装cpu的地方
        self.__rams = []  # 装内存条的地方
        self.__disks = []  # 装硬盘的地方

    def add_cpu(self, cpu):
        if cpu.interface == self.cpu_interface:
            self.__cpu = cpu
        else:
            print("cpu型号不对，不能安装")

    def add_ram(self, ram):
        if len(self.__rams) == self.ram_count:
            print("内存条已经没有位置安装了")
        else:
            self.__rams.append(ram)

    def add_disk(self, disk):
        if len(self.__disks) == self.disk_count:
            print("硬盘已经没有地方安装了")
        else:
            self.__disks.append(disk)

    def run(self):
        if not self.__cpu:
            print("没有cpu，电脑不能正常运行")
            return
        elif len(self.__rams) == 0 or len(self.__rams) > self.ram_count:
            print("内存条安装失败，电脑不能正常运行")
            return
        elif len(self.__disks) == 0 or len(self.__disks) > self.disk_count:
            print("硬盘安装失败，电脑不能正常运行")
            return
        else:
            print("所有配件都安装完毕，电脑正常启动。。。。")


def main():
    # 初始化一台电脑
    computer = Computer("11211", 2, 2)

    # 初始化一个cpu
    cpu = CPU("intel", 4, "11211")

    # 创建两个内存条
    ram1 = RAM("jinshidun", "4G")
    ram2 = RAM("jinshidun", "4G")

    # 创建两个硬盘
    disk1 = RAM("jinshidun", "256G")
    disk2 = RAM("jinshidun", "256G")

    # 组装内存条
    computer.add_ram(ram1)
    computer.add_ram(ram2)

    # 组装cpu
    computer.add_cpu(cpu)

    # 组装硬盘
    computer.add_disk(disk1)
    computer.add_disk(disk2)

    # 让电脑跑起来
    computer.run()


if __name__ == '__main__':
    main()
