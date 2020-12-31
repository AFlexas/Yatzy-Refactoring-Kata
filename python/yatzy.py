class Yatzy:

    @staticmethod
    def chance(*dados):
        return sum(dados)

    @staticmethod
    def yatzy(dados):
        counts = [0]*(max(dados)) 
        for valor in dados:
            counts[valor-1] += 1
        for i in range(max(dados)):
            if counts[i] == (len(dados)):
                return 50
        return 0
    
    @staticmethod
    def ones(*dados):
        sum_of_ones = 0
        for ones in dados:
            if ones == 1:
                sum_of_ones = sum_of_ones + 1
            else:
                pass
        return sum_of_ones
    
    @staticmethod
    def twos(*dados):
        sum_of_twos = 0
        for twos in dados:
            if twos == 2:
                sum_of_twos = sum_of_twos + 2
        return sum_of_twos
    
    @staticmethod
    def threes(*dados):
        sum_of_three = 0
        for threes in dados:
            if threes == 3:
                sum_of_three = sum_of_three + 3
        return sum_of_three
    
    def __init__(self, d1, d2, d3, d4, d5):
        self.dice = [0]*5
        self.dice[0] = d1
        self.dice[1] = d2
        self.dice[2] = d3
        self.dice[3] = d4
        self.dice[4] = d5
    

    def fours(self):
        sum = 0
        for at in range(5):
            if (self.dice[at] == 4): 
                sum += 4
        return sum
    

    def fives(self):
        sum = 0
        for at in range(5):
        # (len(self.dice)): 
            if (self.dice[at] == 5):
                sum = sum + 5
        return sum
    

    def sixes(self):
        sum = 0
        for at in range(len(self.dice)): 
            if (self.dice[at] == 6):
                sum = sum + 6
        return sum
    
    @staticmethod
    def score_pair(*dados):
        counts = [0]*(max(dados))
        for valor in dados:
            counts[valor-1] += 1
        at = 0
        for at in range(max(dados)):
            if (counts[(max(dados))-at-1] == 2):
                return ((max(dados))-at)*2
        return 0
    
    @staticmethod
    def two_pair(*dados):
        counts = [0]*(max(dados))
        for valor in dados:
            counts[valor-1] += 1
        n = 0
        score = 0
        for i in range(max(dados)):
            if (counts[(max(dados))-i-1] >= 2):
                n = n+1
                score += (max(dados)-i)
                    
        if (n == 2):
            return score * 2
        else:
            return 0

    @staticmethod
    def four_of_a_kind(*dados):
        tallies = [0]*(max(dados))
        for valor in dados:
            tallies[valor-1] += 1
        for i in range(max(dados)):
            if (tallies[i] >= 4):
                return (i+1) * 4
        return 0
    

    @staticmethod
    def three_of_a_kind(*dados):
        tallies = [0]*(max(dados))
        for valor in dados:
            tallies[valor-1] += 1
        for i in range(max(dados)):
            if (tallies[i] >= 3):
                return (i+1) * 3
        return 0
        
    

    @staticmethod
    def smallStraight(*dados):
        tallies = [0]*(max(dados))
        for valor in dados:
            tallies[valor-1] += 1
        if (tallies[0] == 1 and
            tallies[1] == 1 and
            tallies[2] == 1 and
            tallies[3] == 1 and
            tallies[4] == 1):
            return 15
        return 0
    

    @staticmethod
    def largeStraight(*dados):
        tallies = [0]*(max(dados))
        for valor in dados:
            tallies[valor-1] += 1
        if (tallies[1] == 1 and
            tallies[2] == 1 and
            tallies[3] == 1 and
            tallies[4] == 1
            and tallies[5] == 1):
            return 20
        return 0
    

    @staticmethod
    def fullHouse(*dados):
        pareja = False
        valor_pareja = 0
        trio = False
        valor_trio = 0
        tallies = [0]*(max(dados))
        for valor in dados:
            tallies[valor-1] += 1

        for i in range(max(dados)):
            if (tallies[i] == 2): 
                pareja = True
                valor_pareja = i+1
            
        for i in range(max(dados)):
            if (tallies[i] == 3): 
                trio = True
                valor_trio = i+1
            
        if (pareja and trio):
            return valor_pareja * 2 + valor_trio * 3
        else:
            return 0
