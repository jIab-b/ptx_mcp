##### 9.7.14.16.10. Report-on operation on mbarrier object

The *report-on* operation on an *mbarrier object* signals miscellaneous information regarding asynchronous operation. For example, such a miscellaneous information can be about errors, warnings encountered; otherwise, it can as well be any extra information conveyed by asynchronous operation.

The miscellaneous information reported by asynchronous operation via *report-on* *mbarrer operation* would be updated in the payload report. The following asynchronous operations can potentially issue *report-on* operation on an associated *mbarrier object*:

- Fabric operations such as `fabric.try_get`, `fabric.try_put`, `fabric.try_red`, `fabric.try_pullred`. Refer to [Fabric Reporting Mechanism](#fabric-reporting-mechanism) for more details.
