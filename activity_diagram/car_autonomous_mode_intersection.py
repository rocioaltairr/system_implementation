class IntersectionLogic:
    def __init__(self):
        self.reached_other_side = False
        self.at_stop_sign = False
        self.others_at_intersection = False
        self.max_cycles = 5 
        self.cycle_count = 0

    def get_intersection_action(self):
        while not self.reached_other_side:
            while not self.at_stop_sign:
                print("Drive forward")
                break
            if self.at_stop_sign:
                print("Stop")
            while self.at_stop_sign and not self.others_at_intersection:
                print("Wait")
                break
            if self.at_stop_sign and self.others_at_intersection:
                print("Drive forward")
            self.cycle_count += 1
            if self.cycle_count >= self.max_cycles:
                print("Finish Cycle")
                return ""
        return "Finish"

if __name__ == "__main__":
    intersection_logic = IntersectionLogic()
