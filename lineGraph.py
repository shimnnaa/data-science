import matplotlib.pyplot as plt
x=[1,2,3,4,5]
y1=[1,4,9,16,25]
y2=[25,20,15,10,5]
plt.plot(x,y1,label='y=x^z',color='green',linestyle='--',marker='x')
plt.plot(x,y2,label='y=30-x^2',color='red',linestyle='--',marker='x')
plt.grid(True)
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Customized Line Plot With Multiple Series')
plt.legend()
plt.savefig('all-features-plot.png')
plt.show()
