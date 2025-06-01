// Funzione per mostrare il form del biglietto e nascondere l'altro
function showTicketForm() {
    document.getElementById('ticket-form').style.display = 'block';
    document.getElementById('subscription-form').style.display = 'none';
}

// Funzione per mostrare il form dell'abbonamento e nascondere l'altro
function showSubscriptionForm() {
    document.getElementById('ticket-form').style.display = 'none';
    document.getElementById('subscription-form').style.display = 'block';
}

// Assicurati che la pagina venga caricata con il form del biglietto attivo di default
document.addEventListener("DOMContentLoaded", function() {
    showTicketForm();
});
