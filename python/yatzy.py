class Yatzy:

    @staticmethod
    def chance(*dado):
        # PONIENDO EL * PERMITE LA ENTRADA DE TODOS LOS ELEMENTOS QUE VENGAN DE INPUT
        # total = 0
        # total += d1
        # total += d2
        # total += d3
        # total += d4
        # total += d5   
        return sum(dado)

    @staticmethod
    def yatzy(dice):
        counts = [0]*(len(dice)+1) # es lo mismo que poner [0]*6 pero como COÑO HAGO QUE NO SE LIMITE A DADOS DE SOLO 6 
        for die in dice:
            counts[die-1] += 1
        for i in range(len(counts)):
            if counts[i] == (len(dice)):
                return 50
        return 0
    # en este refactor simplemente he cambiado la linea 20 en vez de "if counts[i] == 5", si se pone eso solo se aplicaria sobre un yatzy de 5

    
    @staticmethod
    def ones(*searching_one):
        sum_of_ones = 0
        for ones in searching_one:
            if ones == 1:
                sum_of_ones = sum_of_ones + 1
            else:
                pass
        return sum_of_ones
    

    @staticmethod
    def twos(*searching_two):
        sum_of_twos = 0
        for twos in searching_two:
            if twos == 2:
                sum_of_twos = sum_of_twos + 2
        return sum_of_twos
    
    @staticmethod
    def threes(*searching_three):
        sum_of_three = 0
        for threes in searching_three:
            if threes == 3:
                sum_of_three = sum_of_three + 3
        return sum_of_three
    

    def __init__(self, d1, d2, d3, d4, _5):
        self.dice = [0]*5
        self.dice[0] = d1
        self.dice[1] = d2
        self.dice[2] = d3
        self.dice[3] = d4
        self.dice[4] = _5
    

    def fours(self):
        sum = 0
        for at in range(5):
            if (self.dice[at] == 4): 
                sum += 4
        return sum
    

    def fives(self):
        s = 0
        i = 0
        for i in range(len(self.dice)): 
            if (self.dice[i] == 5):
                s = s + 5
        return s
    

    def sixes(self):
        sum = 0
        for at in range(len(self.dice)): 
            if (self.dice[at] == 6):
                sum = sum + 6
        return sum
    
    @staticmethod
    def score_pair(*caras):
        counts = [0]*max(valor)
        for valor in caras:
            counts[valor-1] += 1
        # counts[d2-1] += 1
        # counts[d3-1] += 1
        # counts[d4-1] += 1
        # counts[d5-1] += 1
        at = 0
        for at in range(8):
            if (counts[8-at-1] == 2):
                return (8-at)*2
        return 0
        # Aqui simplemente he cambiado uno a dados para que no sea limitado, pero no acabo de entender como funciona, tiene que haber una mejor manera
        # o almenos mas bonita
    
    @staticmethod
    def two_pair( d1,  d2,  d3,  d4,  d5):
        counts = [0]*6
        counts[d1-1] += 1
        counts[d2-1] += 1
        counts[d3-1] += 1
        counts[d4-1] += 1
        counts[d5-1] += 1
        n = 0
        score = 0
        for i in range(6):
            if (counts[6-i-1] >= 2):
                n = n+1
                score += (6-i)
                    
        if (n == 2):
            return score * 2
        else:
            return 0
    
    @staticmethod
    def four_of_a_kind(*dado):
        tallies = [0]*6
        for caras in dado:
            tallies[caras-1] += 1
        # tallies[_2-1] += 1
        # tallies[d3-1] += 1
        # tallies[d4-1] += 1
        # tallies[d5-1] += 1
        for i in range(6):
            if (tallies[i] >= 4):
                return (i+1) * 4
        return 0
    

    @staticmethod
    def three_of_a_kind( d1,  d2,  d3,  d4,  d5):
        t = [0]*6
        t[d1-1] += 1
        t[d2-1] += 1
        t[d3-1] += 1
        t[d4-1] += 1
        t[d5-1] += 1
        for i in range(6):
            if (t[i] >= 3):
                return (i+1) * 3
        return 0
    

    @staticmethod
    def smallStraight( d1,  d2,  d3,  d4,  d5):
        tallies = [0]*6
        tallies[d1-1] += 1
        tallies[d2-1] += 1
        tallies[d3-1] += 1
        tallies[d4-1] += 1
        tallies[d5-1] += 1
        if (tallies[0] == 1 and
            tallies[1] == 1 and
            tallies[2] == 1 and
            tallies[3] == 1 and
            tallies[4] == 1):
            return 15
        return 0
    

    @staticmethod
    def largeStraight( d1,  d2,  d3,  d4,  d5):
        tallies = [0]*6
        tallies[d1-1] += 1
        tallies[d2-1] += 1
        tallies[d3-1] += 1
        tallies[d4-1] += 1
        tallies[d5-1] += 1
        if (tallies[1] == 1 and
            tallies[2] == 1 and
            tallies[3] == 1 and
            tallies[4] == 1
            and tallies[5] == 1):
            return 20
        return 0
    

    @staticmethod
    def fullHouse( d1,  d2,  d3,  d4,  d5):
        tallies = []
        _2 = False
        i = 0
        _2_at = 0
        _3 = False
        _3_at = 0

        tallies = [0]*6
        tallies[d1-1] += 1
        tallies[d2-1] += 1
        tallies[d3-1] += 1
        tallies[d4-1] += 1
        tallies[d5-1] += 1

        for i in range(6):
            if (tallies[i] == 2): 
                _2 = True
                _2_at = i+1
            

        for i in range(6):
            if (tallies[i] == 3): 
                _3 = True
                _3_at = i+1
            

        if (_2 and _3):
            return _2_at * 2 + _3_at * 3
        else:
            return 0
