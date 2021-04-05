function solution(n) {
    const primeSet = new Set();
    for (let i = 3; i <= n; i += 2) {
      primeSet.add(i);
    }
    primeSet.add(2);
    for (let j = 3; j ** 2 < n; j++) {
      if (primeSet.has(j)) {
        for (let k = j ** 2; k <= n; k += j) {
          primeSet.delete(k);
        }
      }
    }
    return primeSet.size;
  }