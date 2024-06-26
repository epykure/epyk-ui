from epyk.core.js import JsUtils
from epyk.core.py import types
from epyk.core.py import primitives
from epyk.core.js.packages import JsPackage
from epyk.core.js.primitives import JsObjects
from typing import Optional, Union, List, Any


LIB_REF = "rxjs."


def filter(predicate, thisArg = None):
    """Filter items emitted by the source Observable by only emitting those that satisfy a specified predicate.

    `rxjs <https://rxjs.dev/api/operators/filter>`_

    :param predicate: A function that evaluates each value emitted by the source Observable.
    :param thisArg: Optional. Undefined. An optional argument to determine the value of this in the predicate function.
    """
    if thisArg is None:
        return JsUtils.jsWrap("%sfilter(%s)" % (LIB_REF, predicate))

    thisArg = JsUtils.jsConvertData(thisArg, None)
    return JsUtils.jsWrap("%sfilter(%s, %s)" % (LIB_REF, predicate, thisArg))


def first(predicate = None, defaultValue = None):
    """Emits only the first value (or the first value that meets some condition) emitted by the source Observable.

    `rxjs <https://rxjs.dev/api/operators/first>`_

    :param predicate: Optional. Undefined. An optional function called with each item to test for condition matching.
    :param defaultValue: Optional. Undefined. The default value emitted in case no valid value was found on the source.
    """
    if defaultValue is None:
        if predicate is not None:
            return JsUtils.jsWrap("%sfirst(%s)" % (LIB_REF, predicate))

        return JsUtils.jsWrap("%sfirst()" % LIB_REF)

    defaultValue = JsUtils.jsConvertData(defaultValue, None)
    return JsUtils.jsWrap("%sfirst(%s, %s)" % (LIB_REF, predicate, defaultValue))


def last(predicate = None, defaultValue = None):
    """Returns an Observable that emits only the last item emitted by the source Observable.
    It optionally takes a predicate function as a parameter, in which case, rather than emitting the last item from
    the source Observable, the resulting Observable will emit the last item from the source Observable that
    satisfies the predicate.

    `rxjs <https://rxjs.dev/api/operators/first

    :param predicate: Optional. Undefined. An optional function called with each item to test for condition matching.
    :param defaultValue: Optional. Undefined. The default value emitted in case no valid value was found on the source.
    """
    if defaultValue is None:
        if predicate is not None:
            return JsUtils.jsWrap("%slast(%s)" % (LIB_REF, predicate))

        return JsUtils.jsWrap("%slast()" % LIB_REF)

    defaultValue = JsUtils.jsConvertData(defaultValue, None)
    return JsUtils.jsWrap("%slast(%s, %s)" % (LIB_REF, predicate, defaultValue))


def map(expr: types.JS_DATA_TYPES):
    """Applies a given project function to each value emitted by the source Observable,
    and emits the resulting values as an Observable.
    """
    return JsUtils.jsWrap("%smap(%s)" % (LIB_REF, expr))


def skip(count: float):
    """Returns an Observable that skips the first count items emitted by the source Observable.

    `rxjs <https://rxjs.dev/api/operators/skip>`_

    :param count: The number of times, items emitted by source Observable should be skipped.
    """
    return JsUtils.jsWrap("%sskip(%s)" % (LIB_REF, count))


def skipLast(count: float):
    """Skip a specified number of values before the completion of an observable.

    `rxjs <https://rxjs.dev/api/index/function/skipLast>`_

    :param count: Number of elements to skip from the end of the source Observable.
    """
    return JsUtils.jsWrap("%sskipLast(%s)" % (LIB_REF, count))


def skipUntil(notifier):
    """Returns an Observable that skips items emitted by the source Observable until a second Observable emits an item.

    `rxjs <https://rxjs.dev/api/index/function/skipUntil>`_

    :param notifier: An ObservableInput that has to emit an item before the source Observable elements begin to be mirrored by the resulting Observable.
    """
    return JsUtils.jsWrap("%sskipUntil(%s)" % (LIB_REF, notifier))


def scan(expr: types.JS_DATA_TYPES):
    """Useful for encapsulating and managing state.
    Applies an accumulator (or "reducer function") to each value from the source after an initial state is established
    -- either via a seed value (second argument), or from the first value from the source.

    `rxjs <https://rxjs.dev/api/index/function/scan>`_
    """
    return JsUtils.jsWrap("%sscan(%s)" % (LIB_REF, expr))


def startWith(values):
    """Returns an observable that, at the moment of subscription, will synchronously emit all values provided to this
    operator, then subscribe to the source and mirror all of its emissions to subscribers.

    `rxjs <https://rxjs.dev/api/operators/startWith>`_
    """
    return JsUtils.jsWrap("%sstartWith(%s)" % (LIB_REF, values))


def take(count: int):
    """Emits only the first count values emitted by the source Observable.

    `rxjs <https://rxjs.dev/api/operators/take>`_

    :param count: The maximum number of next values to emit.
    """
    return JsUtils.jsWrap("%stake(%s)" % (LIB_REF, count))


def takeLast(count: int):
    """Waits for the source to complete, then emits the last N values from the source, as specified by the count argument.

    `rxjs <https://rxjs.dev/api/operators/takeLast>`_

    :param count: The maximum number of values to emit from the end of the sequence of values emitted by the source Observable.
    """
    return JsUtils.jsWrap("%stakeLast(%s)" % (LIB_REF, count))


def throttleTime(duration: int):
    """Emits a value from the source Observable, then ignores subsequent source values for duration milliseconds,
    then repeats this process.

    `rxjs <https://rxjs.dev/api/index/function/throttleTime>`_
    """
    return JsUtils.jsWrap("%sthrottleTime(%s)" % (LIB_REF, duration))


def concatAll():
    """Converts a higher-order Observable into a first-order Observable by concatenating the inner Observables in order.

    `rxjs <https://rxjs.dev/api/operators/concatAll>`_
    """
    return JsUtils.jsWrap("%sconcatAll()" % LIB_REF)


def mergeAll():
    """Subscribes to each inner Observable as it arrives, then emits each value as it arrives.

    `rxjs <https://rxjs.dev/api/operators/mergeAll>`_
    """
    return JsUtils.jsWrap("%smergeAll()" % LIB_REF)


def distinct(keySelector = None, flushes = None):
    """Filtering Operators.

    Returns an Observable that emits all items emitted by the source Observable that are distinct by comparison from
    previous items.

    `rxjs <https://rxjs.dev/api/operators/distinct>`_

    :param keySelector: Optional. undefined. Optional function to select which value you want to check as distinct
    :param flushes: Optional. undefined.Optional ObservableInput for flushing the internal HashSet of the operator
    """
    if keySelector is None and flushes is None:
        return JsUtils.jsWrap("%sdistinct()" % LIB_REF)


class Observer:

    def next(self, value: types.JS_DATA_TYPES):
        """A callback function that gets called by the producer during the subscription when the producer "has" the
        value. It won't be called if error or complete callback functions have been called, nor after the consumer
        has unsubscribed.

        `rxjs <https://rxjs.dev/api/index/interface/Observer#error>`_

        :param value:
        """
        return JsUtils.jsWrap(value)

    def error(self, value: types.JS_DATA_TYPES):
        """A callback function that gets called by the producer if and when it encountered a problem of any kind.
        The errored value will be provided through the err parameter.
        This callback can't be called more than one time, it can't be called if the complete callback function have
        been called previously, nor it can't be called if the consumer has unsubscribed.

        `rxjs <https://rxjs.dev/api/index/interface/Observer#error>`_

        :param value:
        """
        return JsUtils.jsWrap(value)

    def complete(self, value: types.JS_DATA_TYPES):
        """A callback function that gets called by the producer if and when it has no more values to provide (by calling
        next callback function). This means that no error has happened.
        This callback can't be called more than one time, it can't be called if the error callback function have
        been called previously, nor it can't be called if the consumer has unsubscribed.

        `rxjs <https://rxjs.dev/api/index/interface/Observer#complete>`_

        :param value:
        """
        return JsUtils.jsWrap(value)


class Subscriber(Observer):
    ...


class Unsubscribable:

    def unsubscribe(self):
        """

        `rxjs <https://rxjs.dev/api/index/interface/Unsubscribable#unsubscribe>`_
        """
        return JsUtils.jsWrap("unsubscribe()")


class SubscriptionLike(Unsubscribable):

    @property
    def closed(self):
        """A flag to indicate whether this Subscription has already been unsubscribed.

        `rxjs <https://rxjs.dev/api/index/interface/SubscriptionLike>`_
        """
        return JsUtils.jsWrap("closed")


class Subscription(SubscriptionLike):

    def __init__(self, selector: str):
        self._selector = selector

    def unsubscribe(self):
        """Disposes the resources held by the subscription. May, for instance, cancel an ongoing Observable execution or
        cancel any other type of work that started when the Subscription was created.

        `rxjs <https://rxjs.dev/api/index/class/Subscription#unsubscribe>`_
        """
        return JsUtils.jsWrap("%s.unsubscribe()" % self.varId)

    @property
    def varId(self):
        """The Javascript and Python reference ID. """
        return self._selector

    def add(self, teardown):
        """Adds a finalizer to this subscription, so that finalization will be unsubscribed/called when this subscription
        is unsubscribed.

        `rxjs <https://rxjs.dev/api/index/class/Subscription#unsubscribe>`_

        :param teardown: The finalization logic to add to this subscription
        """
        return JsUtils.jsWrap("%s.add(%s)" % (self.varId, teardown))

    def remove(self, teardown):
        """Removes a finalizer from this subscription that was previously added with the add method.

        `rxjs <https://rxjs.dev/api/index/class/Subscription#remove>`_

        :param teardown: The finalization logic to remove to this subscription
        """
        return JsUtils.jsWrap("%s.remove(%s)" % (self.varId, teardown))

    def toStr(self) -> str:
        return self.varId


class Observable(Subscriber):

    def __init__(self, selector: str):
        self._selector = selector
        self.__chain = []

    @classmethod
    def new(cls, expr: str, id: str, var_type: str = "const"):
        """Define an observable object.

        Usage::

            page.js.rxjs.Observable.new("(subscriber) => {console.log('Hello'); subscriber.next(42);}", "foo"),

        `rxjs <https://rxjs.dev/guide/observable>`_
        """
        return JsUtils.jsWrap("%s %s = new %sObservable(%s)" % (var_type, id, LIB_REF, expr))

    @classmethod
    def get(cls, id: str):
        """Get an Observable object by reference.

        Usage::

            page.js.rxjs.Observable.get("foo").subscribe("(x) => {console.log(x)}")

        `rxjs <ttps://rxjs.dev/guide/observable>`_
        """
        return Observable(id)

    @property
    def varId(self):
        """The Javascript and Python reference ID. """
        return self._selector

    def forEach(self, value) -> JsObjects.JsPromise:
        """Used as a NON-CANCELLABLE means of subscribing to an observable, for use with APIs that expect promises,
        like async/await. You cannot unsubscribe from this.

        `rxjs <https://rxjs.dev/api/index/class/Observable#foreach>`_
        """
        return JsObjects.JsPromise(value)

    def pipe(self, *args):
        """Used to stitch together functional operators into a chain.

        `rxjs <https://rxjs.dev/api/index/class/Observable#pipe>`_
        """
        self.__chain.append("pipe(%s)" % ", ".join([arg.toStr() for arg in args]))
        return self

    def toPromise(self):
        """Subscribe to this Observable and get a Promise resolving on complete with the last emission (if any).

        `rxjs <https://rxjs.dev/api/index/class/Observable#topromise>`_
        """
        return JsObjects.JsPromise()

    def subscribe(self, observerOrNext = None) -> Subscription:
        """Invokes an execution of an Observable and registers Observer handlers for notifications it will emit.

        :param observerOrNext: Optional. Default is undefined.
        """
        if isinstance(observerOrNext, list):
            return Subscription("%s.subscribe(() => {%s})" % (
                self.toStr(), JsUtils.jsConvertFncs(observerOrNext, toStr=True)))

        return Subscription("%s.subscribe(%s)" % (self.toStr(), observerOrNext))

    def toStr(self):
        if self.__chain:
            value = "%s.%s" % (self.varId, ".".join(self.__chain))
            self.__chain = []
            return value

        return "%s" % self.varId


class Subject(Observable, SubscriptionLike):

    @property
    def isStopped(self):
        """

        `rxjs <https://rxjs.dev/api/index/class/Subject>`_
        """
        return JsUtils.jsWrap("isStopped")

    @property
    def hasError(self):
        """

        `rxjs <https://rxjs.dev/api/index/class/Subject>`_
        """
        return JsUtils.jsWrap("hasError")


def fromEvent(target, eventName: str, options = None, resultSelector = None) -> Observable:
    """Creates an Observable that emits events of a specific type coming from the given event target.

    Usage::

        btn = page.ui.button("Click Me !")
        page.body.onReady([
          page.js.rxjs.fromEvent(btn, "click").subscribe([
            page.js.console.log("Clicked 1!")
          ])
        ])

    `rxjs <https://rxjs.dev/api/index/function/fromEvent>`_

    :param target: The DOM EventTarget, Node.js EventEmitter, JQuery-like event target, NodeList or HTMLCollection to attach the event handler to.
    :param eventName: The event name of interest, being emitted by the target.
    :param options: Optional. Undefined. Options to pass through to the underlying addListener, addEventListener or on functions.
    :param resultSelector: Optional. Undefined. A mapping function used to transform events. It takes the arguments from the event handler and should return a single value.
    """
    eventName = JsUtils.jsConvertData(eventName, None)
    if hasattr(target, "dom"):
        return Observable("%sfromEvent(%s, %s)" % (LIB_REF, target.dom.varId, eventName))

    return Observable("%sfromEvent(%s, %s)" % (LIB_REF, target, eventName))


def interval(number: int, scheduler = None) -> Observable:
    """Creates an Observable that emits sequential numbers every specified interval of time, on a specified SchedulerLike.

    `rxjs <https://rxjs.dev/api/index/function/interval>`_

    :param number: Optional. 0. The interval size in milliseconds (by default) or the time unit determined by the scheduler's clock.
    :param scheduler: Optional. asyncScheduler. The SchedulerLike to use for scheduling the emission of values, and providing a notion of "time".
    """
    if scheduler is None:
        return Observable("%sinterval(%s)" % (LIB_REF, number))


def of(*args) -> Observable:
    """Converts the arguments to an observable sequence.

    `rxjs <https://rxjs.dev/api/index/function/of>`_

    :param args: A comma separated list of arguments you want to be emitted
    """
    return Observable("%sof(%s)" % (LIB_REF, ", ".join(args)))


def range(start: int, count: int, scheduler = None) -> Observable:
    """Creates an Observable that emits a sequence of numbers within a specified range.

    `rxjs <https://rxjs.dev/api/index/function/range>`_

    :param start: The value of the first integer in the sequence
    :param count: Optional. Undefined. The number of sequential integers to generate
    :param scheduler: Optional. Undefined. A SchedulerLike to use for scheduling the emissions of the notifications
    """
    return Observable("%srange(%s, %s)" % (LIB_REF, start, count))


def ii(expression: str, trueResult: Observable, falseResult: Observable):
    """Checks a boolean at subscription time, and chooses between one of two observable sources

    `rxjs <https://rxjs.dev/api/index/function/iif>`_

    :param expression: Condition which Observable should be chosen
    :param trueResult: An Observable that will be subscribed if condition is true
    :param falseResult: An Observable that will be subscribed if condition is false
    """
    return Observable("%siif(%s, %s, %s)" % (LIB_REF, expression, trueResult, falseResult))


def timer(due: int, scheduler = None):
    """Creates an observable that will wait for a specified time period, or exact date, before emitting the number 0.

    `rxjs <https://rxjs.dev/api/index/function/timer>`_

    :param due: If a number, the amount of time in milliseconds to wait before emitting. If a Date, the exact time at which to emit.
    :param scheduler: Optional. Undefined. The scheduler to use to schedule the delay. Defaults to asyncScheduler.
    """
    return Observable("%stimer(%s, %s)" % (LIB_REF, due, scheduler))


def concatAll(project, resultSelector = None):
    """Transformation Operators.

    Projects each source value to an Observable which is merged in the output Observable,
    in a serialized fashion waiting for each one to complete before merging the next.
    """
    if resultSelector is None:
        return Observable("%sconcatAll(%s)" % (LIB_REF, project))
