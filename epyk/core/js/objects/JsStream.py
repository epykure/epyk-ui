
from epyk.core.js import JsUtils

from epyk.core.js.packages import JsPackage
from epyk.core.js.primitives import JsObjects


class TeedStreams(object):

  def __init__(self, varId):
    self.varId = varId

  @property
  def stream_0(self):
    return ReadableStream("%s[0]" % self.varId)

  @property
  def stream_1(self):
    return ReadableStream("%s[1]" % self.varId)


class TransformStream(JsPackage):

  @property
  def readable(self):
    """

    Related Pages:
    --------------
    https://developer.mozilla.org/en-US/docs/Web/API/TransformStream

    :return:
    """
    return "%s.readable" % self.varId

  @property
  def writable(self):
    """

    Related Pages:
    --------------
    https://developer.mozilla.org/en-US/docs/Web/API/TransformStream
    """
    return "%s.writable" % self.varId


class ReadableStream(JsPackage):

  @property
  def locked(self):
    return JsObjects.JsPromise("%s.locked" % self.varId)

  def cancel(self):
    """
    Description:
    ------------
    The cancel() method of the ReadableStream interface cancels the associated stream.
    The supplied reason parameter will be given to the underlying source, which may or may not use it.

    Related Pages:
    --------------
    https://developer.mozilla.org/en-US/docs/Web/API/ReadableStream/cancel
    """
    return self.fnc("cancel()")

  def getReader(self):
    """
    Description:
    ------------
    The getReader() method of the ReadableStream interface creates a reader and locks the stream to it.
    While the stream is locked, no other reader can be acquired until this one is released.

    Related Pages:
    --------------
    https://developer.mozilla.org/en-US/docs/Web/API/ReadableStream/getReader
    """
    return ReadableStream("%s.getReader()" % self.varId)

  def pipeThrough(self, transformStream, options=None):
    """
    Description:
    ------------
    The pipeThrough() method of the ReadableStream interface provides a chainable way of piping the current stream through a transform stream or any other writable/readable pair.

    Related Pages:
    --------------
    https://developer.mozilla.org/en-US/docs/Web/API/ReadableStream/pipeThrough

    :param transformStream: A TransformStream (or an object with the structure {writable, readable}) consisting of a readable stream and a writable stream working together to transform some data from one form to another.
    :param options: The options that should be used when piping to the writable stream. Available options are
                      - preventClose
                      - preventAbort
                      - preventCancel
                      - signal
    """
    if options is None:
      return TransformStream("%s.pipeThrough(%s)" % (self.varId, transformStream))

    return TransformStream("%s.pipeThrough(%s, %s)" % (self.varId,transformStream, options))

  def pipeTo(self, destination, options=None):
    """
    Description:
    ------------
    The pipeTo() method of the ReadableStream interface pipes the current ReadableStream to a given WritableStream and returns a promise that fulfills when the piping process completes successfully, or rejects if any errors were encountered.

    Related Pages:
    --------------
    https://developer.mozilla.org/en-US/docs/Web/API/ReadableStream/pipeTo

    Attributes:
    ----------
    :param destination:
    :param options:
    """
    if options is None:
      return WritableStream("%s.pipeTo(%s)" % (self.varId, destination))

    return WritableStream("%s.pipeTo(%s, %s)" % (self.varId, destination, options))

  def tee(self):
    """
    Description:
    ------------
    The tee() method of the ReadableStream interface tees the current readable stream, returning a two-element array containing the two resulting branches as new ReadableStream instances.

    Related Pages:
    --------------
    https://developer.mozilla.org/en-US/docs/Web/API/ReadableStream/tee
    """
    return TeedStreams("%s.tee()" % self.varId)


class WritableStreamDefaultWriter(JsPackage):

  @property
  def desiredSize(self):
    """
    Description:
    ------------
    The desiredSize read-only property of the WritableStreamDefaultWriter interface returns the desired size required to fill the stream's internal queue.

    Related Pages:
    --------------
    https://developer.mozilla.org/en-US/docs/Web/API/WritableStreamDefaultWriter/desiredSize
    """
    return "%s.desiredSize" % self.varId

  @property
  def writer(self):
    """
    Description:
    ------------
    The closed read-only property of the WritableStreamDefaultWriter interface returns a promise that fulfills if the stream becomes closed or the writer's lock is released, or rejects if the stream errors.

    Related Pages:
    --------------
    https://developer.mozilla.org/en-US/docs/Web/API/WritableStreamDefaultWriter/closed
    """
    return JsObjects.JsPromise("%s.writer" % self.varId)

  @property
  def ready(self):
    """
    Description:
    ------------
    The ready read-only property of the WritableStreamDefaultWriter interface returns a Promise that resolves when the desired size of the stream's internal queue transitions from non-positive to positive, signaling that it is no longer applying backpressure.

    Related Pages:
    --------------
    https://developer.mozilla.org/en-US/docs/Web/API/WritableStreamDefaultWriter/ready
    """
    return JsObjects.JsPromise("%s.ready" % self.varId)

  def abort(self, reason=None):
    """
    Description:
    ------------
    The abort() method of the WritableStreamDefaultWriter interface aborts the stream, signaling that the producer can no longer successfully write to the stream and it is to be immediately moved to an error state, with any queued writes discarded.

    Related Pages:
    --------------
    https://developer.mozilla.org/en-US/docs/Web/API/WritableStreamDefaultWriter/abort
    """
    if reason is None:
      return JsObjects.JsPromise("%s.abort()" % self.varId)

    reason = JsUtils.jsConvertData(reason, None)
    return JsObjects.JsPromise("%s.abort(%s)" % (self.varId, reason))

  def close(self):
    """
    Description:
    ------------
    The close() method of the WritableStreamDefaultWriter interface closes the associated writable stream.

    Related Pages:
    --------------
    https://developer.mozilla.org/en-US/docs/Web/API/WritableStreamDefaultWriter/close
    """
    return JsObjects.JsPromise("%s.close()" % self.varId)

  def releaseLock(self):
    """
    Description:
    ------------
    The releaseLock() method of the WritableStreamDefaultWriter interface releases the writer's lock on the corresponding stream.

    Related Pages:
    --------------
    https://developer.mozilla.org/en-US/docs/Web/API/WritableStreamDefaultWriter/releaseLock
    """
    return self.fnc_closure("%s.releaseLock()" % self.varId)

  def write(self, chunk):
    """
    Description:
    ------------
    The write() property of the WritableStreamDefaultWriter interface writes a passed chunk of data to a WritableStream and its underlying sink, then returns a Promise that resolves to indicate the success or failure of the write operation.

    Related Pages:
    --------------
    https://developer.mozilla.org/en-US/docs/Web/API/WritableStreamDefaultWriter/write

    Attributes:
    ----------
    :param chunk: A block of binary data to pass to the WritableStream.
    """
    chunk = JsUtils.jsConvertData(chunk, None)
    return JsObjects.JsPromise("%s.write(%s)" % (self.varId, chunk))


class WritableStream(JsPackage):

  @property
  def locked(self):
    """
    Description:
    ------------
    https://developer.mozilla.org/en-US/docs/Web/API/WritableStream
    """
    return "%s.locked" % self.varId

  def abort(self, reason=None):
    """
    Description:
    ------------
    The abort() method of the WritableStream interface aborts the stream, signaling that the producer can no longer successfully write to the stream and it is to be immediately moved to an error state, with any queued writes discarded.

    Related Pages:
    --------------
    https://developer.mozilla.org/en-US/docs/Web/API/WritableStream/abort
    """
    if reason is None:
      return JsObjects.JsPromise("%s.abort()" % self.varId)

    reason = JsUtils.jsConvertData(reason, None)
    return JsObjects.JsPromise("%s.abort(%s)" % (self.varId, reason))

  def close(self):
    return self.fnc_closure("close()")

  def getWriter(self):
    """
    Description:
    ------------
    The getWriter() method of the WritableStream interface returns a new instance of WritableStreamDefaultWriter and locks the stream to that instance. While the stream is locked, no other writer can be acquired until this one is released.

    Related Pages:
    --------------
    https://developer.mozilla.org/en-US/docs/Web/API/WritableStream/getWriter
    """
    return WritableStreamDefaultWriter("%s.getWriter()" % self.varId)


if __name__ == '__main__':
  obj = ReadableStream().cancel()
  print(obj.toStr())
