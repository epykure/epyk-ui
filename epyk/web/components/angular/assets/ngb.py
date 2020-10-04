
from epyk.web.components.angular.assets import asset


class DatePicker(asset.Asset):
  name = 'bt-datepicker'
  imports = {"@ng-bootstrap/ng-bootstrap": ["NgbDateStruct", "NgbCalendar"]}

  def __str__(self):
    return '''
<input class="form-control" placeholder="yyyy-mm-dd" name="dp" [(ngModel)]="model" ngbDatepicker #d="ngbDatepicker">
'''


class ProgressBar(asset.Asset):
  name = 'bt-progressbar'

  def __str__(self):
    return '''
<p><ngb-progressbar type="info" [value]="50"></ngb-progressbar></p>
'''


class Rating(asset.Asset):
  name = 'bt-rating'

  def __str__(self):
    return '''
<ngb-rating [(rate)]="currentRate"></ngb-rating>
'''


class TimePicker(asset.Asset):
  name = 'bt-timepicker'

  def __str__(self):
    return '''
<ngb-timepicker [(ngModel)]="time"></ngb-timepicker>
'''


class Toast(asset.Asset):
  name = 'bt-toast'

  def __str__(self):
    return '''
<ngb-toast header="Hello" [autohide]="false">
  I am a simple static toast with a header.
</ngb-toast>
'''