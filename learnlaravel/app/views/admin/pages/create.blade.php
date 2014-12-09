@extends('admin._layout.default')

@section('main')

    <h2>Add Page</h2>

    {{ Notification::showAll() }}

    @if ($errors->any())
        <div class="alert alert-error">
            {{ implode('<br>', $errors->all()) }}
        </div>    

    @endif

    {{ Form::open(array('route' => 'admin.pages.store')) }}
        <div class="control-group">
            {{ Form::label('title', 'Title') }}
            <div class="controls">
                {{ Form::text('title') }}
            </div>
        </div>

        <div class="control-group">
            {{ Form::label('body', 'content') }}
            <div class="controls">
                {{ Form::textarea('body') }}
            </div>
        </div>

        <div class="form-actions">
            {{ Form::submit('Add', array('class' => 'btn btn-success btn-save btn-large')) }}
            <a href="{{URL::route('admin.pages.index') }}" class="btn btn-large">Cancle</a>
        </div>  

    {{ Form::close()}}
@stop