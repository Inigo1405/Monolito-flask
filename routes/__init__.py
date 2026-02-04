from flask import Flask, render_template, url_for, flash, redirect, Blueprint

blueprintA = Blueprint('blueprintA', __name__,url_prefix='/autenticacion')
blueprintB = Blueprint('blueprintB', __name__,url_prefix='/productos')
