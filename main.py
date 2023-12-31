def count_batteries_by_health(present_capacities):
  healthy=0
  exchange=0
  failed=0
 
  for i in present_capacities:
   

    soh=100*i/120
    # print(soh)
    soh=int(soh)
    # print(soh)

    if soh>80 and soh<=100:
      healthy+=1
    elif soh>=65 and soh<=80:
      exchange+=1
    elif soh<65:
      failed+=1
  print(healthy,exchange,failed)
  return {
    "healthy": healthy,
    "exchange": exchange,
    "failed": failed
    }
  
  
def test_bucketing_by_health():
  print("Counting batteries by SoH...\n")
  present_capacities = [115, 118, 80, 95, 91, 77]
  counts = count_batteries_by_health(present_capacities)
  assert(counts["healthy"] == 2)
  assert(counts["exchange"] == 3)
  assert(counts["failed"] == 1)
  print("Done counting :)")


if __name__ == '__main__':
  test_bucketing_by_health()

