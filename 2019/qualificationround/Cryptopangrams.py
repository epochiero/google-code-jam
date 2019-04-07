import math

class Cryptopangrams:

    def main(self):
        testcases = int(input())
        for t in range(testcases):
            max_number, length = [int(x) for x in input().split(" ")]
            all_ciphers = [int(x) for x in input().split(" ")]

            # First, get prime factors in order, so:
            # prime_factors_in_order[0]*prime_factors_in_order[1] = first letter
            # prime_factors_in_order[1]*prime_factors_in_order[2] = second letter
            # etc.
            largest_prime_factor_first_cipher = self.get_largest_prime_factor(all_ciphers[0])
            other_prime_factor = all_ciphers[0] // largest_prime_factor_first_cipher

            options = [
                (largest_prime_factor_first_cipher, other_prime_factor),
                (other_prime_factor, largest_prime_factor_first_cipher)
            ]

            found = False
            current_option = 0
            while not found:
                try:
                    prime_factors_in_order = []
                    prime_factors_in_order.extend(options[current_option])
                    previous_prime = prime_factors_in_order[1]
                    for cipher in all_ciphers[1:]:
                        other_prime = cipher // previous_prime
                        previous_prime = other_prime
                        prime_factors_in_order.append(previous_prime)

                    # Then, order the primes and assign them a letter to each
                    ordered_primes = sorted(set(prime_factors_in_order))
                    letter_map = {}
                    for i, prime in enumerate(ordered_primes):
                        letter_map[prime] = chr(i+65)

                    # Generate the word
                    possible_values = [letter_map[prime] for prime in prime_factors_in_order]
                    generated_ciphers = []
                    for l in range(length):
                        generated_ciphers.append(prime_factors_in_order[l]*prime_factors_in_order[l+1])
                    if generated_ciphers == all_ciphers:
                        # Found
                        found = True
                        word = "".join([letter_map[prime] for prime in prime_factors_in_order])
                        print("Case #{}: {}".format(t+1, word))
                        if t+1 < testcases:
                            print("\n")
                except ZeroDivisionError:
                    current_option = 1
                    continue
                current_option = 1

    def get_largest_prime_factor(self, number):
        largest_prime = 2
        while largest_prime**2 <= number:
            if number % largest_prime:
                largest_prime += 1
            else:
                number //= largest_prime
        return number

program = Cryptopangrams()
program.main()
