import time
import re
import subprocess


class Monitor(object):
    def __init__(self):
        self.INTERVAL = 1

    @staticmethod
    def get_uptime():
        f = open('/proc/uptime', 'r')
        uptime = f.readline()
        f.close()
        uptime = uptime.split('.', 2)
        get_time = int(uptime[0])
        return int(get_time)

    @staticmethod
    def get_memory():
        re_parser = re.compile(r'^(?P<key>\S*):\s*(?P<value>\d*)\s*kB')
        result = dict()
        for line in open('/proc/meminfo'):
            match = re_parser.match(line)
            if not match:
                continue
            key, value = match.groups(['key', 'value'])
            result[key] = int(value)

        mem_total = float(result['MemTotal'])
        mem_free = float(result['MemFree'])
        cached = float(result['Cached'])
        mem_used = mem_total - (cached + mem_free)
        swap_total = float(result['SwapTotal'])
        swap_free = float(result['SwapFree'])

        return int(mem_total), int(mem_used), int(swap_total), int(swap_free)

    @staticmethod
    def get_hdd():
        p = subprocess.check_output(
            ['df', '-Tlm', '--total', '-t', 'ext4', '-t', 'ext3', '-t', 'ext2', '-t', 'reiserfs', '-t', 'jfs', '-t',
             'ntfs',
             '-t', 'fat32', '-t', 'btrfs', '-t', 'fuseblk', '-t', 'zfs', '-t', 'simfs', '-t', 'xfs']).decode("Utf-8")
        total = p.splitlines()[-1]
        used = total.split()[3]
        size = total.split()[2]
        return int(size), int(used)

    @staticmethod
    def get_time():
        stat_file = open("/proc/stat", "r")
        time_list = stat_file.readline().split(' ')[2:6]
        stat_file.close()
        for i in range(len(time_list)):
            time_list[i] = int(time_list[i])
        return time_list

    def delta_time(self):
        x = self.get_time()
        time.sleep(self.INTERVAL)
        y = self.get_time()
        for i in range(len(x)):
            y[i] -= x[i]
        return y

    def get_cpu(self):
        t = self.delta_time()
        st = sum(t)
        if st == 0:
            st = 1
        result = 100 - (t[len(t) - 1] * 100.00 / st)
        return round(result)

    @staticmethod
    def load_stat():
        """
        CPU负载监控
        """
        loadavg = {}
        f = open("/proc/loadavg")
        con = f.read().split()
        f.close()
        loadavg['lavg_1'] = con[0]
        loadavg['lavg_5'] = con[1]
        loadavg['lavg_15'] = con[2]
        loadavg['nr'] = con[3]

        prosess_list = loadavg['nr'].split('/')
        loadavg['running_prosess'] = prosess_list[0]
        loadavg['total_prosess'] = prosess_list[1]

        loadavg['last_pid'] = con[4]

        return loadavg

    def get_info(self):
        uptime = self.get_uptime()
        memory_total, memory_used, swap_total, swap_free = self.get_memory()
        hdd_total, hdd_used = self.get_hdd()
        cpu = self.get_cpu()

        data = {}
        tim = str(int(uptime / 3600)) + ' 小时'
        data['uptime'] = tim
        data['memory_total'] = memory_total
        data['memory_used'] = memory_used
        data['swap_total'] = swap_total
        data['swap_used'] = swap_total - swap_free

        data['hdd_total'] = hdd_total
        data['hdd_used'] = hdd_used
        data['cpu'] = cpu
        data['load'] = self.load_stat()

        return data


if __name__ == '__main__':
    monitor = Monitor()
    print(monitor.get_info())
