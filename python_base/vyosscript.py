import vymgmt

#连接设备
vyos = vymgmt.Router('172.200.100.230', user='vyos', password='vyos', port=22)
vyos.login()
vyos.configure()
try:
    vyos.set("protocols static route 203.0.113.0/25 next-hop 192.0.2.20")
    vyos.set("protocols static route 202.0.113.0/25 next-hop 192.0.2.20")

except Exception as e:
    print('this is error log',e)

finally:
    vyos.set("protocols static route 209.0.113.0/25 next-hop 192.0.2.20")
    vyos.commit()
    vyos.save()
    vyos.exit()
    vyos.logout()



