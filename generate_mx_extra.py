import cadquery as cq
from ols import keycap


if 'show_object' in locals():
    show_object(keycap(unitX=2.75))
    
if __name__ == '__main__':
    def run(u, name, **kwargs):
        args1 = dict(kwargs)
        del args1['cut']
        k = keycap(unitX=u, **args1)
        kc = keycap(unitX=u, **kwargs).rotate((0,0,0),(1,0,0),90)
        cq.exporters.export(k, f'generated/mx-extra/{name}-{u}u.stl', tolerance=0.001, angularTolerance=0.05)
        cq.exporters.export(kc, f'generated/mx-extra/{name}-{u}u-cut.stl', tolerance=0.001, angularTolerance=0.05)
        cq.exporters.export(k, f'generated/mx-extra/{name}-{u}u.step')
        cq.exporters.export(kc, f'generated/mx-extra/{name}-{u}u-cut.step')
    def r3c(u):
        return run(u, 'ols-v1-r3c', depth=-1.0, cut=True)
    def r3(u):
        return run(u, 'ols-v1-r3', cut=True)
    def r2(u):
        return run(u, 'ols-v1-r2', angle=-6, height=5.5, cut=0.8)
    def r2c(u):
        return run(u, 'ols-v1-r2c', angle=-6, depth=-1.0, height=5.5, cut=0.8)
    def r4(u):
        return run(u, 'ols-v1-r4', angle=6, height=5.5, cut=0.4)
    def r2cv(u):
        return run(1, 'ols-v1-r2c-v', unitY=u, angle=-6, depth=-1.0, height=5.5, cut=0.8)
    import concurrent.futures
    with concurrent.futures.ProcessPoolExecutor() as executor:
        print(executor._max_workers)
        executor.map(r3c, (1.0, 1.25, 1.5, 1.75, 2.0, 2.25, 2.5, 2.75, 3.0, 6.25, 7.0))
        executor.map(r3, (1.25, 1.5, 1.75, 2.0, 2.25, 2.5, 2.75, 3.0, 6.25, 7.0))
        executor.map(r2, (1.25, 1.5, 1.75, 2.0, 2.25, 2.5, 2.75, 3.0, 6.25, 7.0))
        executor.map(r2c, (1.0, 1.25, 1.5, 1.75, 2.0, 2.25, 2.5, 2.75, 3.0, 6.25, 7.0))
        executor.map(r4, (1.25, 1.5, 1.75, 2.0, 2.25, 2.5, 2.75, 3.0, 6.25, 7.0))
        executor.map(r2cv, (1.25, 1.5, 1.75, 2.0))
