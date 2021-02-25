                print(i)
                t2 = threading.Thread(target=self.add_to_list, args=[i])
                t2.start()
                lust.append(t2)